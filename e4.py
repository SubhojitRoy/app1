import webbrowser

user_term = input("Enter a search term: ")

# webbrowser.open("https://www.google.com/search?q=")
# webbrowser.open("https://www.google.com/search?q=python+website")

webbrowser.open("https://www.google.com/search?q=" + user_term)