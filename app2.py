import streamlit as st

st.title("Hello :green[Everyone]")
st.header("Iam pardhasai")
st.subheader("Welcome to my app")
st.snow()

btn_click=st.button("click here to connect")
if btn_click==True:
    st.balloons()

    linkedin="https://www.linkedin.com/in/pardhasai-nalathuru-44817018a/"
    var1=st.write(format(linkedin))