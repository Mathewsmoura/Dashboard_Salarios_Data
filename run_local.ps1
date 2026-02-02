# Script PowerShell para executar localmente com porta 5000
$env:STREAMLIT_SERVER_PORT = "5000"
$env:STREAMLIT_SERVER_ADDRESS = "localhost"
streamlit run src/app.py
