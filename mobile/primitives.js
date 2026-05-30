export const PRIMITIVES = {
  SELF:  { syllable: 'sa', key: 'F', emoji: '👤', meaning: 'I, me, my',           color: '#4CAF50' },
  OTHER: { syllable: 'to', key: 'D', emoji: '👥', meaning: 'you, they, it',        color: '#2196F3' },
  NOT:   { syllable: 'na', key: 'J', emoji: '❌', meaning: 'no, negation',          color: '#F44336' },
  WANT:  { syllable: 'wu', key: 'K', emoji: '🤲', meaning: 'desire, need',          color: '#FF9800' },
  GOOD:  { syllable: 'go', key: 'S', emoji: '✅', meaning: 'positive, correct',     color: '#8BC34A' },
  BAD:   { syllable: 'bi', key: 'L', emoji: '⚠️', meaning: 'negative, wrong',       color: '#FF5722' },
  NOW:   { syllable: 'ne', key: 'G', emoji: '⚡', meaning: 'present, immediate',    color: '#FFC107' },
  HERE:  { syllable: 'hi', key: 'H', emoji: '📍', meaning: 'this place',            color: '#00BCD4' },
  ALIVE: { syllable: 'li', key: 'E', emoji: '💚', meaning: 'living, conscious',     color: '#4CAF50' },
  MOVE:  { syllable: 'mo', key: 'R', emoji: '➡️', meaning: 'motion, action',        color: '#9C27B0' },
  WATER: { syllable: 'du', key: 'I', emoji: '💧', meaning: 'liquid, fluid',         color: '#03A9F4' },
  AIR:   { syllable: 're', key: 'O', emoji: '🌬️', meaning: 'gas, breath, sky',      color: '#B3E5FC' },
  HEAT:  { syllable: 'fu', key: 'W', emoji: '🔥', meaning: 'temperature, fire',     color: '#FF5722' },
  SOLID: { syllable: 'ko', key: 'V', emoji: '🪨', meaning: 'object, earth, hard',   color: '#795548' },
  LIGHT: { syllable: 'lu', key: 'N', emoji: '☀️', meaning: 'brightness, visible',   color: '#FFEB3B' },
  THINK: { syllable: 'te', key: 'U', emoji: '💭', meaning: 'know, understand',      color: '#E91E63' },
};

export const NAMES = Object.keys(PRIMITIVES);

// Acquisition tiers — learn in this order
export const TIERS = [
  ['SELF', 'OTHER', 'NOT', 'WANT'],
  ['GOOD', 'BAD', 'NOW', 'HERE'],
  ['ALIVE', 'MOVE', 'THINK', 'WATER'],
  ['AIR', 'HEAT', 'SOLID', 'LIGHT'],
];
