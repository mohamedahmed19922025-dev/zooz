# main.py
import streamlit as st
import pandas as pd
st.title("hello")

df = pd.read_excel("55.xlsx")
event = st.dataframe(
    df,
    column_config=column_configuration,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
)
                   


