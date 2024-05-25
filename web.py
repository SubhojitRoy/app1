import streamlit as st
from modules import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("My To-Do App")
st.write("This is a simple comment")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="write your todo...",
              on_change=add_todo, key="new_todo")
