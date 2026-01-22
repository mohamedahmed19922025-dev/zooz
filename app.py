# main.py
import streamlit as st
import pandas as pd
st.title("hello")

df = pd.read_excel("55.xlsx")
st.write(df.head)
                   

