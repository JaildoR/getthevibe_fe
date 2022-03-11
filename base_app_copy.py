import base64
import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
import json

#config
img = Image.open('streamlit-img/haut_de_page.jpg')
st.set_page_config(page_title = 'Get The Vibe', page_icon = img)

#title of the app
logo = Image.open('streamlit-img/get the vibe .png')
st.image(logo)

#hiding 'made with streamlit'
hide_ad = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_ad, unsafe_allow_html = True)

#diff pages for image or camera photo
page_names = ['File Uploader', 'Camera Photo']
page = st.radio('Choose one', page_names)

if page == 'File Uploader':
    #file downloader
    file= st.file_uploader("", type=["png","jpg","jpeg"])

    #shows the picture if there is one
    if file == None :
        st.write('No image')
    else:
        file_bytes = file.getvalue()
        image = Image.open(file)
        st.image(image, width = 400)
        if st.button('😀 Get the vibe 😀'):
            gif = st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
            url = 'https://vibe-opf4327g5q-ew.a.run.app/vibecheck'
            headers = {'Content-Type': 'application/json',
               'Accept': 'text/plain'}

            file_post = {'file': file_bytes}
            response = requests.post(url, headers,files = file_post)
            results = response.content.decode('utf-8')
            results = json.loads(results)
            if results :
                del gif
                st.header('The emotion is:')
                st.subheader(results["emotion"])
            else:
                pass

else :
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture)
        if st.button('😀 Get the vibe 😀'):
            st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
            url = 'https://vibe-opf4327g5q-ew.a.run.app/vibecheck'
            headers = {'Content-Type': 'application/json',
               'Accept': 'text/plain'}
            file_post = {'file': picture}
            response = requests.post(url, headers,files = file_post)
            results = response.content.decode('utf-8')
            results = json.loads(results)
            st.header('The emotion is:')
            st.subheader(results["emotion"])

#changing button color
#m = st.markdown("""
#<style>
#div.stButton > button:first-child {
#    background-color: #233067
#}
#</style>""", unsafe_allow_html=True)
