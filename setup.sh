mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#00525b'
backgroundColor = '#eeb2b0'
secondaryBackgroundColor = '#e58986'
textColor= '#00474f'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
