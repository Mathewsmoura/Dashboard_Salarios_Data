#!/usr/bin/env bash
# Script shell para executar localmente com porta 5000
export STREAMLIT_SERVER_PORT=5000
export STREAMLIT_SERVER_ADDRESS=localhost
streamlit run src/app.py
