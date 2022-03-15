mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#0097A7'
backgroundColor = '#D9534F'
secondaryBackgroundColor = '#D9534F'
textColor= '##00474f'
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
