mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#d6d0d0'
backgroundColor='#d9534f'
secondaryBackgroundColor='#e17672'
textColor='#ffffff'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
