import React, { useState, useEffect, useRef } from 'react';
import {
  View, Text, StyleSheet, TouchableOpacity, ScrollView,
  Animated, Dimensions, SafeAreaView, StatusBar,
} from 'react-native';
import * as Speech from 'expo-speech';
import * as Haptics from 'expo-haptics';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { PRIMITIVES, NAMES, TIERS } from './primitives';

const { width } = Dimensions.get('window');
const CARD_SIZE = (width - 48) / 4;

// ── Learner model ─────────────────────────────────────────────────────────────

const defaultModel = () =>
  Object.fromEntries(NAMES.map(n => [n, { acquired: false, correct: 0, attempts: 0 }]));

async function loadModel() {
  try {
    const raw = await AsyncStorage.getItem('learner_model');
    return raw ? JSON.parse(raw) : defaultModel();
  } catch { return defaultModel(); }
}

async function saveModel(model) {
  await AsyncStorage.setItem('learner_model', JSON.stringify(model));
}

function acquiredList(model) {
  return NAMES.filter(n => model[n].acquired);
}

function nextToTeach(model) {
  for (const tier of TIERS)
    for (const p of tier)
      if (!model[p].acquired) return p;
  return null;
}

function recordAttempt(model, primitive, correct) {
  const m = { ...model, [primitive]: { ...model[primitive] } };
  m[primitive].attempts += 1;
  if (correct) m[primitive].correct += 1;
  const rate = m[primitive].correct / m[primitive].attempts;
  if (rate >= 0.8 && m[primitive].attempts >= 5) m[primitive].acquired = true;
  return m;
}

// ── Speech ────────────────────────────────────────────────────────────────────

function saySyllable(name) {
  Speech.speak(PRIMITIVES[name].syllable, { rate: 0.7, pitch: 1.0 });
}

function saySequence(names) {
  const text = names.map(n => PRIMITIVES[n].syllable).join('  ');
  Speech.speak(text, { rate: 0.65, pitch: 1.0 });
}

// ── Primitive Card ────────────────────────────────────────────────────────────

function PrimitiveCard({ name, onPress, size = CARD_SIZE, dim = false, highlight = false }) {
  const p = PRIMITIVES[name];
  const scale = useRef(new Animated.Value(1)).current;

  const handlePress = () => {
    Animated.sequence([
      Animated.timing(scale, { toValue: 0.88, duration: 80, useNativeDriver: true }),
      Animated.timing(scale, { toValue: 1,    duration: 120, useNativeDriver: true }),
    ]).start();
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
    onPress(name);
  };

  return (
    <Animated.View style={{ transform: [{ scale }] }}>
      <TouchableOpacity
        style={[
          styles.card,
          { width: size, height: size + 12 },
          highlight && { borderColor: p.color, borderWidth: 2.5 },
          dim && { opacity: 0.3 },
        ]}
        onPress={handlePress}
        activeOpacity={0.85}
      >
        <Text style={styles.cardEmoji}>{p.emoji}</Text>
        <Text style={[styles.cardName, { color: p.color }]}>{name}</Text>
        <Text style={styles.cardSyl}>{p.syllable}</Text>
      </TouchableOpacity>
    </Animated.View>
  );
}

// ── Progress Bar ──────────────────────────────────────────────────────────────

function ProgressBar({ model }) {
  const done = acquiredList(model).length;
  const pct = done / NAMES.length;
  return (
    <View style={styles.progressWrap}>
      <View style={[styles.progressBar, { width: `${pct * 100}%` }]} />
      <Text style={styles.progressText}>{done}/{NAMES.length} acquired</Text>
    </View>
  );
}

// ══════════════════════════════════════════════════════════════════════════════
// LEARN SCREEN
// ══════════════════════════════════════════════════════════════════════════════

function LearnScreen({ model }) {
  const teaching = nextToTeach(model);
  const acquired = new Set(acquiredList(model));

  return (
    <ScrollView contentContainerStyle={styles.grid}>
      <Text style={styles.hint}>Tap a primitive to hear it spoken</Text>
      {teaching && (
        <View style={styles.teachBanner}>
          <Text style={styles.teachText}>
            Now learning: {PRIMITIVES[teaching].emoji} {teaching} — say "{PRIMITIVES[teaching].syllable}"
          </Text>
          <TouchableOpacity onPress={() => saySyllable(teaching)}>
            <Text style={styles.teachPlay}>🔊 Hear it</Text>
          </TouchableOpacity>
        </View>
      )}
      <View style={styles.cardGrid}>
        {NAMES.map(name => (
          <PrimitiveCard
            key={name}
            name={name}
            onPress={saySyllable}
            highlight={name === teaching}
            dim={!acquired.has(name) && name !== teaching}
          />
        ))}
      </View>
      <TouchableOpacity
        style={styles.helloWorld}
        onPress={() => saySequence(['HERE', 'OTHER', 'ALIVE', 'HERE'])}
      >
        <Text style={styles.hwLabel}>Hello World  🔊</Text>
        <Text style={styles.hwCode}>hi · to · li · hi</Text>
        <Text style={styles.hwMeaning}>HERE · OTHER · ALIVE · HERE</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

// ══════════════════════════════════════════════════════════════════════════════
// QUIZ SCREEN
// ══════════════════════════════════════════════════════════════════════════════

function QuizScreen({ model, setModel }) {
  const pool = [...acquiredList(model), nextToTeach(model)].filter(Boolean);
  const [target, setTarget] = useState(null);
  const [result, setResult] = useState(null);
  const [score, setScore] = useState({ correct: 0, total: 0 });

  const newQuestion = (currentPool) => {
    const p = currentPool || pool;
    if (!p.length) return;
    const t = p[Math.floor(Math.random() * p.length)];
    setTarget(t);
    setResult(null);
    setTimeout(() => saySyllable(t), 200);
  };

  useEffect(() => { if (pool.length > 0) newQuestion(); }, []);

  const handleAnswer = (name) => {
    if (!target || result) return;
    const correct = name === target;
    const newModel = recordAttempt(model, target, correct);
    setModel(newModel);
    saveModel(newModel);
    setScore(s => ({ correct: s.correct + (correct ? 1 : 0), total: s.total + 1 }));
    setResult({ correct, target });
    if (correct) {
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
      Speech.speak('good', { rate: 0.8 });
    } else {
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
      setTimeout(() => saySyllable(target), 400);
    }
    const updatedPool = [...acquiredList(newModel), nextToTeach(newModel)].filter(Boolean);
    setTimeout(() => newQuestion(updatedPool), 1500);
  };

  if (pool.length < 2) return (
    <View style={styles.center}>
      <Text style={styles.hint}>Go to Learn and tap a few primitives first!</Text>
    </View>
  );

  return (
    <View style={{ flex: 1, paddingTop: 8 }}>
      <View style={styles.quizHeader}>
        <TouchableOpacity style={styles.playBtn} onPress={() => target && saySyllable(target)}>
          <Text style={styles.playBtnText}>🔊 Play again</Text>
        </TouchableOpacity>
        <Text style={styles.scoreText}>{score.correct}/{score.total}</Text>
      </View>
      <Text style={styles.quizPrompt}>Which primitive was that?</Text>
      {result && (
        <Text style={[styles.resultText, { color: result.correct ? '#4CAF50' : '#F44336' }]}>
          {result.correct
            ? '✅  Correct!'
            : `❌  ${result.target} · "${PRIMITIVES[result.target].syllable}"`}
        </Text>
      )}
      <View style={styles.cardGrid}>
        {pool.map(name => (
          <PrimitiveCard
            key={name}
            name={name}
            onPress={handleAnswer}
            highlight={!!(result && name === result.target)}
          />
        ))}
      </View>
    </View>
  );
}

// ══════════════════════════════════════════════════════════════════════════════
// BUILD SCREEN
// ══════════════════════════════════════════════════════════════════════════════

function BuildScreen() {
  const [sequence, setSequence] = useState([]);

  const add = (name) => {
    saySyllable(name);
    setSequence(s => [...s, name]);
  };

  return (
    <ScrollView contentContainerStyle={{ padding: 12 }}>
      <Text style={styles.hint}>Build a sentence — tap primitives in order</Text>
      <View style={styles.sequenceRow}>
        {sequence.length === 0
          ? <Text style={styles.seqEmpty}>tap below to build...</Text>
          : sequence.map((n, i) => (
            <View key={i} style={[styles.seqChip, { borderColor: PRIMITIVES[n].color }]}>
              <Text style={styles.seqChipText}>{PRIMITIVES[n].emoji} {PRIMITIVES[n].syllable}</Text>
            </View>
          ))
        }
      </View>
      <View style={styles.seqButtons}>
        <TouchableOpacity
          style={styles.seqBtn}
          onPress={() => { if (sequence.length) saySequence(sequence); }}
        >
          <Text style={styles.seqBtnText}>🔊 Speak all</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.seqBtn, { backgroundColor: '#2a1a1a' }]}
          onPress={() => setSequence(s => s.slice(0, -1))}
        >
          <Text style={[styles.seqBtnText, { color: '#F44336' }]}>⌫ Back</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.seqBtn, { backgroundColor: '#1a1d23' }]}
          onPress={() => setSequence([])}
        >
          <Text style={[styles.seqBtnText, { color: '#888' }]}>✕ Clear</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.cardGrid}>
        {NAMES.map(name => (
          <PrimitiveCard key={name} name={name} onPress={add} />
        ))}
      </View>
      <View style={{ height: 20 }} />
    </ScrollView>
  );
}

// ══════════════════════════════════════════════════════════════════════════════
// MAIN APP
// ══════════════════════════════════════════════════════════════════════════════

export default function App() {
  const [model, setModel] = useState(defaultModel());
  const [tab, setTab] = useState('learn');

  useEffect(() => { loadModel().then(setModel); }, []);

  const tabs = [
    { key: 'learn', label: '📚 Learn' },
    { key: 'quiz',  label: '🎯 Quiz'  },
    { key: 'build', label: '🔨 Build' },
  ];

  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar barStyle="light-content" />
      <View style={styles.header}>
        <Text style={styles.headerTitle}>PrimaTap</Text>
        <ProgressBar model={model} />
      </View>
      <View style={{ flex: 1 }}>
        {tab === 'learn' && <LearnScreen model={model} />}
        {tab === 'quiz'  && <QuizScreen  model={model} setModel={setModel} />}
        {tab === 'build' && <BuildScreen />}
      </View>
      <View style={styles.tabBar}>
        {tabs.map(t => (
          <TouchableOpacity
            key={t.key}
            style={[styles.tabBtn, tab === t.key && styles.tabBtnActive]}
            onPress={() => setTab(t.key)}
          >
            <Text style={[styles.tabLabel, tab === t.key && styles.tabLabelActive]}>
              {t.label}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
    </SafeAreaView>
  );
}

// ── Styles ────────────────────────────────────────────────────────────────────

const styles = StyleSheet.create({
  safe:           { flex: 1, backgroundColor: '#0e1117' },
  header:         { paddingHorizontal: 16, paddingTop: 8, paddingBottom: 6 },
  headerTitle:    { color: '#fff', fontSize: 22, fontWeight: '700', letterSpacing: 1 },

  progressWrap:   { height: 16, backgroundColor: '#1a1d23', borderRadius: 8,
                    marginTop: 6, overflow: 'hidden' },
  progressBar:    { height: '100%', backgroundColor: '#4CAF50', borderRadius: 8 },
  progressText:   { position: 'absolute', width: '100%', textAlign: 'center',
                    color: '#fff', fontSize: 10, lineHeight: 16 },

  hint:           { color: '#666', textAlign: 'center', marginVertical: 10, fontSize: 13 },
  center:         { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 24 },

  grid:           { padding: 12 },
  cardGrid:       { flexDirection: 'row', flexWrap: 'wrap', gap: 5,
                    justifyContent: 'center', paddingVertical: 8 },
  card:           { backgroundColor: '#1a1d23', borderRadius: 12, alignItems: 'center',
                    justifyContent: 'center', borderWidth: 1, borderColor: '#2a2d33', margin: 2 },
  cardEmoji:      { fontSize: 22 },
  cardName:       { fontSize: 8, fontWeight: '800', marginTop: 2, letterSpacing: 0.5 },
  cardSyl:        { fontSize: 14, color: '#ddd', fontWeight: '700', marginTop: 1 },

  teachBanner:    { backgroundColor: '#0d2010', borderRadius: 12, padding: 12,
                    marginBottom: 8, alignItems: 'center' },
  teachText:      { color: '#4CAF50', textAlign: 'center', fontSize: 14 },
  teachPlay:      { color: '#4CAF50', fontSize: 16, marginTop: 6 },

  helloWorld:     { alignItems: 'center', marginTop: 20, padding: 18,
                    backgroundColor: '#1a1d23', borderRadius: 16,
                    borderWidth: 1, borderColor: '#2a2d33' },
  hwLabel:        { color: '#666', fontSize: 12, marginBottom: 6 },
  hwCode:         { color: '#fff', fontSize: 22, fontWeight: '700', letterSpacing: 4 },
  hwMeaning:      { color: '#555', fontSize: 11, marginTop: 4 },

  quizHeader:     { flexDirection: 'row', justifyContent: 'space-between',
                    alignItems: 'center', paddingHorizontal: 16, paddingBottom: 8 },
  playBtn:        { backgroundColor: '#1a1d23', paddingHorizontal: 18,
                    paddingVertical: 8, borderRadius: 20 },
  playBtnText:    { color: '#4CAF50', fontSize: 15 },
  scoreText:      { color: '#666', fontSize: 15 },
  quizPrompt:     { color: '#bbb', textAlign: 'center', fontSize: 16, marginBottom: 6 },
  resultText:     { textAlign: 'center', fontSize: 16, fontWeight: '700',
                    marginBottom: 8, paddingHorizontal: 16 },

  sequenceRow:    { minHeight: 56, flexDirection: 'row', flexWrap: 'wrap', gap: 6,
                    backgroundColor: '#1a1d23', borderRadius: 12, padding: 10,
                    marginBottom: 10, alignItems: 'center' },
  seqEmpty:       { color: '#333', fontSize: 14 },
  seqChip:        { borderWidth: 1.5, borderRadius: 8, paddingHorizontal: 8, paddingVertical: 4 },
  seqChipText:    { color: '#ddd', fontSize: 14 },
  seqButtons:     { flexDirection: 'row', gap: 8, marginBottom: 10 },
  seqBtn:         { flex: 1, backgroundColor: '#0d2010', borderRadius: 10,
                    padding: 10, alignItems: 'center' },
  seqBtnText:     { color: '#4CAF50', fontSize: 13, fontWeight: '600' },

  tabBar:         { flexDirection: 'row', backgroundColor: '#1a1d23', paddingBottom: 8,
                    paddingTop: 6, borderTopWidth: 1, borderTopColor: '#2a2d33' },
  tabBtn:         { flex: 1, alignItems: 'center', paddingVertical: 6 },
  tabBtnActive:   { borderTopWidth: 2, borderTopColor: '#4CAF50' },
  tabLabel:       { color: '#555', fontSize: 12 },
  tabLabelActive: { color: '#4CAF50', fontWeight: '700' },
});
