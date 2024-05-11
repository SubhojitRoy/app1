# from functions import read_todos, write_todos
from modules import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("Time is below: ")
print(now)
print("It is: ", now)
while True:
    """ Get user input and strip space chars from it """
    print("Choose your options from below")
    print("add or new, show or display, edit and the number, complete and the number, exit")
    user_action = input("Choose your option: ")
    user_action = user_action.strip()

    # Check if user inputs add
    # if "add" in user_action or "new" in user_action:
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]
        # Call read_todos function
        todos = functions.read_todos()
        # Add input to the variable
        todos.append(todo + "\n")
        # Call write_todos function
        functions.write_todos(todos)

    # Check if user inputs show
    # elif "show" in user_action or "display" in user_action:
    elif user_action.startswith("show") or user_action.startswith("display"):
        # Call read_todos function
        todos = functions.read_todos()
        # For indexing and printing the todos
        for index, item in enumerate(todos):
            # For removing extra whitespaces and specified characters
            item = item.strip('\n')
            # To capitalize all the first letter of the words of the sentence
            item = item.title()
            print(f"{index + 1} - {item}")
            # row = f"{index + 1} - {item}"
            # print(row)

    # Check if user inputs edit
    # elif "edit" in user_action:
    elif user_action.startswith("edit"):
        try:
            # Get input of todos number to edit
            # number = int(input("Number of the todos to edit: "))
            number = int(user_action[5:])
            print(number)
            # Make index number less by 1
            number = number - 1
            # Call read_todos function
            todos = functions.read_todos()
            # Print existing todos of the number
            existing_todos = todos[number]
            print(existing_todos)
            # Input the new todos
            new_todo = input("Enter your todo: ")
            # Print index number by adding 1
            print(number + 1)
            # Print the new todo
            print(new_todo)
            # Write the new todo by index number
            todos[number] = new_todo + '\n'
            # Call write_todos function
            functions.write_todos(todos)
        except ValueError:
            print("Please enter edit and the number.")
            continue
        except IndexError:
            print("No item found with that number.")
            continue

    # Check if user inputs complete
    # elif "complete" in user_action or "remove" in user_action:
    elif user_action.startswith("complete"):
        try:
            # Enter the number of todo to remove
            number = int(user_action[8:])
            # Call read_todos function
            todos = functions.read_todos()
            # Take the variable from the index, put it on a variable and remove the todo
            index = number - 1
            todo_remove = todos[index].strip('\n')
            todos.pop(index)
            # Print the todo is removed
            print(f"{todo_remove} is removed from the Todo list.")
            # Call write_todos function
            functions.write_todos(todos)
            # For indexing and printing the todos
            for index, item in enumerate(todos):
                # For removing extra whitespaces and specified characters
                item = item.strip('\n')
                # To capitalize all the first letter of the words of the sentence
                item = item.title()
                print(f"{index + 1} - {item}")
        except ValueError:
            print("Please enter complete and the number.")
            continue
        except IndexError:
            print("No item found with that number.")
            continue

    # Check if user inputs exit
    # elif "exit" in user_action:
    elif user_action.startswith("exit"):
        break

    else:
        print("Unknown command entered")

    # Check if user inputs anything except add, show, edit, complete or exit
    # if whatever in user_action:
    #     print("Invalid input")
print("bye!")
