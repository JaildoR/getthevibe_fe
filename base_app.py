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

#file downloader
file= st.file_uploader("", type=["png","jpg","jpeg"])

#shows the picture if there is one
if file == None :
    st.write('No image')
else:
    # file_details = {"filename":file.name, "filetype":file.type,
    #                          "filesize (in MB)":file.size / 1000000}
    # st.write(file_details)

    file_bytes = file.getvalue()
    image = Image.open(file)
    st.image(image, width = 400)
#uploading image from your camera
st.header('or upload directly from your camera:')
picture = st.camera_input("Take a picture")
if picture:
     st.image(picture)

#hiding 'made with streamlit'
hide_ad = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_ad, unsafe_allow_html = True)

if st.button('Check the vibe'):
    url = 'https://vibe-opf4327g5q-ew.a.run.app/vibecheck'
    headers = {'Content-Type': 'application/json',
               'Accept': 'text/plain'}

    file_post = {'file': file_bytes}
    response = requests.post(url, headers,files = file_post)
    results = response.content.decode('utf-8')
    results = json.loads(results)
    st.header('The emotion is:')
    st.subheader(results["emotion"])
else:
    pass
