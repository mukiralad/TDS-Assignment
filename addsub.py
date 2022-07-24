import streamlit as st

st.title("Division Streamlit Assignment")

st.write("For determining the Division result")

a = st.number_input("Enter the number you want to Divide from")

b = st.number_input("Enter the number you want to Divide")

st.write(a/b)
