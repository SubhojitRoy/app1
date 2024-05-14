from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.read_todos(), key="todos",
                     enable_events=True, size=(44, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window("My To-Do App",
                   [[label], [input_box, add_button],
                    [listbox, edit_button, complete_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    # print(values['todos'])
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            existing_todos = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.read_todos()
            index = todos.index(existing_todos)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            existing_todos = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.read_todos()
            index = todos.index(existing_todos)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()



