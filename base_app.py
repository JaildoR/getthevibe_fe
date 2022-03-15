from sklearn.covariance import empirical_covariance
import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
import ast

#config
img = Image.open('streamlit-img/Happy face logo.png')
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

    # diff pages for image or camera photo
    # page_names = ['File Uploader', 'Camera Photo']
    # page = st.radio('Choose one', page_names)
with col3:
    pass


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
            url = 'https://vibefull-opf4327g5q-ew.a.run.app/vibecheck'
            headers = {'Content-Type': 'application/json',
            'Accept': 'text/plain'}
            file_post = {'file': file_bytes}
            response = requests.post(url, headers,files = file_post)
            st.image(response.content)
            emotion_df = response.headers.get('emotion_df')
            emotion_df = pd.DataFrame.from_dict((ast.literal_eval(emotion_df)))
            emotion_df = emotion_df.reset_index(drop=True)
            st.dataframe(emotion_df)
            gif.empty()


else :
    picture = st.camera_input("")
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
            emotion_df = response.headers.get('emotion_df')
            emotion_df = pd.DataFrame.from_dict((ast.literal_eval(emotion_df)))
            st.dataframe(emotion_df)
            gif.empty()


#just adding some space
for i in range(1, 50):
    ""

#image and name for each team member
st.subheader('Meet the team !')
col1, col2, col3, col4 = st.columns(4)
with col1 :
    name = st.write('Jaildo Rocha')
    image = st.image('https://avatars.githubusercontent.com/u/10917858?v=4')
with col2:
    name = st.write('Pilar Figueroa')
    image = st.image('https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1639069068/evekemjngwcak2wn2ybh.jpg')
with col3:
    name = st.write('Jasper Anger')
    image = st.image('https://avatars.githubusercontent.com/u/96623311?v=4')
with col4:
    name = st.write('Eric Coccoli')
    image = st.image('https://avatars.githubusercontent.com/u/97439521?v=4')
