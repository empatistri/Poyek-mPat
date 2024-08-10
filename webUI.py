import os
import streamlit as st
from streamlit_option_menu import option_menu

# import pandas as pd
import numpy as np

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ['Home', 'Tools', 'Settings'],
    )

if selected == 'Home':
    if not 'out' in os.listdir('.'):
        try:
            os.system('mkdir out')
            print('folder berhasil dibuat')
        except:
            print('folder gagal dibuat')
    else:
        print('folder sudah ada')

    lisFolder = os.listdir('.')

    st.title('Home')
    st.dataframe(lisFolder, use_container_width=True)

def download(link):
    try:
        os.system(f"yt-dlp -o './out/%(title)s' -x {link}")
        print('berhasil unduh')
    except:
        print('gagal unduh')
    

if selected == 'Tools':
    st.title('Tools')
    col1, col2 = st.columns(2)

    with col1:
        linkYutub = st.text_input('Link Yutub')
        if st.button('Cari File'):
            download(linkYutub)
            st.warning('berhasil unduh')
        with col2:
            file = os.listdir('./out')
            for i in file:
                if i.endswith('.opus'):
                    st.write(i)
                    if st.download_button('Download Opus', i, i):
                        os.system(f'rm ./out/"{i}"')
                        st.rerun()

if selected == 'Settings':
    st.title('Settings')
    