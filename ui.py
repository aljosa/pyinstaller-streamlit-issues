import streamlit as st

TEXT = None

def init():
    global TEXT
    TEXT = st.empty()