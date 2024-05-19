import streamlit as st
from modules import functions

todos = functions.read_todos()


st.title("My To-Do App")
st.subheader("My To-Do App")
st.write("This is a simple comment")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="write your todo...")
