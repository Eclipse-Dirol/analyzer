import streamlit as st
list_file = [".txt"]
st.title("This is my analyzer")
select = st.selectbox("file:", list_file)
x = st.chat_input("input")
if x == None:
    pass
else:
    st.success(x)