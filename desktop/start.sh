#!/bin/bash
cd "$(dirname "$0")"
echo "Starting PrimaTap..."
echo "Opening in browser at http://localhost:8501"
python3 -m streamlit run app.py --server.headless false
