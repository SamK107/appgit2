import streamlit as st 
import pandas as pd 

st.set_page_config(layout='wide')
def app():
    col1, col2, col3 = st.columns((0.4, 0.5, 0.2))
    var_an = col1.selectbox("", options=[2023, 2022], label_visibility='collapsed', key="k1")
    var_lib = col2.text_input("", label_visibility='collapsed',  key="k2")
    
    button = st.button("Enregistrer", key='enre')
    if button:
        st.write(var_an, var_lib)
    