# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print("Enter Your Birth Date:")
# print("\n")
# user_text = input("Enter Your Birth Date:\n")
# print("\n")
# print("Your Birth Date is:")
# print(user_text)

# user_text = input("Enter Your Birth Date: ")
# print("\n")
# # print(user_text)
# print("Your Birth Date is: " + user_text)

# prompt = "Enter Your Birth Date: "
# user_text = input(prompt)
# print("\n")
# # print(user_text)
# print("Your Birth Date is: " + user_text)
# print("Your Birth Date is: ", user_text)

# user_prompt = "ToDoList: "
# ToDoList1 = input(user_prompt)
# ToDoList2 = input(user_prompt)
# ToDoList3 = input(user_prompt)
# print("\n")
# # print(user_text)
# # ToDoList = [ToDoList1, ToDoList2, ToDoList3]
# # print(ToDoList)
# print("ToDoList1: " + ToDoList1)
# print("ToDoList2: " + ToDoList2)
# print("ToDoList3: " + ToDoList3)

# name = input("What is your name?\nEnter your name: ")
# while True:
#     print(name.capitalize())

# while True:
#     name = input("What is your name?\nEnter your name: ")
#     print("My name is: " + name.upper())

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)

# password = input("Enter Your Password: ")
# while password!="pass123":
#     print("Incorrect Password")
#     password = input("Enter Your Password: ")
# print("Correct Password")

# todos = []
# print("Enter exit to logout")
# while True:
#     user_action = input("Enter add or show: ")
#     match user_action:
#         case "add":
#             todo = input("Enter your todo: ")
#             todos.append(todo)
#         case "show":
#             print(todos)
#         case "exit":
#             break
# print("bye!")

# todos = []
# print("Enter exit to logout")
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        # Check if user inputs add
        case "add":
            todo = input("Enter your todo: ") + "\n"
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # Check if user inputs show
        case "show" | "display":
            # file = open('todos.txt', 'r')
            # # Open function writes in a file
            # todos = file.readlines()
            # file.close()
            # Open function writes in a file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(todos)

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index + 1} - {item}")
                # row = f"{index + 1}-{item}"
                # print(row)

            # for index, item in enumerate(todos):
            #     item = item.title()
            #     print(f"{index + 1} - {item}")
            #     # row = f"{index + 1}-{item}"
            #     # print(row)

        # Check if user inputs edit
        case "edit":
            # Get input of todos number to edit
            number = int(input("Number of the todos to edit: "))
            number = number - 1

            # Read the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Print existing todos of the number
            existing_todos = todos[number]
            print(existing_todos)

            # Input the new todos
            new_todo = input("Enter your todo: ")
            print(new_todo)
            todos[number] = new_todo + '\n'

            # Write in the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # Check if user inputs complete
        case "complete":
            # for index, item in enumerate(todos):
            #     row = f"{index + 1} - {item}"
            #     print(row)
            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index + 1} - {item}")
            # Enter the number of todo to remove
            number = int(input("Number of the todos to complete: "))
            # Read the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # todos.pop(number - 1)
            index = number - 1
            todo_remove = todos[index].strip('\n')
            todos.pop(index)
            # Print the todo is removed
            message = f"{todo_remove} is removed from the Todo list."
            print(message)
            # Write in the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            # Print Todos
            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index + 1} - {item}")

        # Check if user inputs exit
        case "exit":
            break



        # Check if user inputs anything except add, show, edit, complete or exit
        case whatever:
            print("Invalid input")
print("bye!")

date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 5? ")
thought = input("Let your thoughts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thought + "\n")