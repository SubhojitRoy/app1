date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 5?\n1. very bad\n2. bad\n3. average\n4. good\n5. very good\nEnter your choice: ")
thought = input("Let your thoughts flow:\n")

# For main file
# with open(f"journal/{date}.txt", "w") as file:

# For file in elsewhere
with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thought + "\n")