# main.py
import streamlit as st
import pandas as pd
st.title("hello")

df = pd.read_excel("55.xlsx")
event = st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
)
if st.button("Delete Selected Rows"):
    if event and "selection" in event and "rows" in event["selection"]:
        selected = event["selection"]["rows"]
        df = df.drop(index=selected).reset_index(drop=True)
        df.to_excel("55.xlsx", index=False)
        st.rerun()
    else:
        st.warning("No rows selected!")                  




