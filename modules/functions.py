FILEPATH = "todos.txt"


# Function for opening and reading the file
def read_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_read = file.readlines()
    return todos_read


""" DOC String
Used for writing documentations
"""


# Function for opening and writing the file
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())