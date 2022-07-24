import streamlit as st

st.title("Subtraction Streamlit Assignment")

st.write("For determining the subtraction result")

a = st.number_input("Enter the number you want to subtract from")

b = st.number_input("Enter the number you want to subtract")

st.write(a-b)