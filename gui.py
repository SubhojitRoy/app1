from modules import functions
import PySimpleGUI as sg


label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   [[label], [input_box, add_button]],
                   font='Helvetica')

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.read()
window.close()
