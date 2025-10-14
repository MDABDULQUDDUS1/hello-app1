import streamlit as st
import openai
import datetime

st.title("Welcome to the Chat bot:")
user_input = st.text_input("Play with me:")

st.write("You entered:",user_input )