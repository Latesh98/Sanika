# Create a list of string of varied length and display the length of individual string in list

string_list = [
    "Hello",
    "World",
    "Python programming",
    "Tanmay Gurav",
    "I am DON TEGGY",
    "SOCKET IP CCN ",
    "Regular expressions",
    "Length check"
]

# Display the length of each string in the list
for string in string_list:
    print(f'"{string}" has length: {len(string)}')
