import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
import json
import logging

#config
img = Image.open('streamlit-img/haut_de_page.jpg')
st.set_page_config(page_title = 'Get The Vibe', page_icon = img, layout="centered")
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
#

with open('css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# body
col1, col2, col3 = st.columns(3)

with col1:
    pass
with col2:
    page_names = ['File Uploader', 'Camera Photo']
    page = st.select_slider("",options=page_names)

    #diff pages for image or camera photo
    # page_names = ['File Uploader', 'Camera Photo']
    #page = st.radio('Choose one', page_names)
with col3:
    pass

def anim(gif):
    gif = st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
    if not results:
        return gif
    else :
        gif = ""
        return gif


def clear_picture():
    st.session_state["picture"] = None

if page == 'File Uploader':
    #file downloader
    file= st.file_uploader("", type=["png","jpg","jpeg"])
    #shows the picture if there is one
    if file == None :
        pass
    else:
        file_bytes = file.getvalue()
        image = Image.open(file)
        st.image(image, width = 400)
        if st.button('😀 Get the vibe 😀'):
            gif = st.markdown('<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" class="loading">', unsafe_allow_html=True)
            url = 'https://vibe-opf4327g5q-ew.a.run.app/vibecheck'
            headers = {'Content-Type': 'application/json',
            'Accept': 'text/plain'}
            file_post = {'file': file_bytes}
            response = requests.post(url, headers,files = file_post)
            results = response.content.decode('utf-8')
            gif.empty()
            results = json.loads(results)
            st.header('I detect...')
            st.subheader(results["emotion"])


else :
    picture = st.camera_input("Take a picture")
    if picture:
        #st.image(picture)
        if st.button('😀 Get the vibe 😀', on_click=clear_picture):
            gif = st.markdown('<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif" class="loading">', unsafe_allow_html=True)
            url = 'https://vibefull-opf4327g5q-ew.a.run.app/vibecheck'
            headers = {'Content-Type': 'application/json',
            'Accept': 'text/plain'}
            file_post = {'file': picture}
            response = requests.post(url, headers,files = file_post)
            st.image(response.content)
            gif.empty()
