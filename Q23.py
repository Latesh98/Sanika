#23. Count Number of words in given file

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


file_path = 'path/to/your/file.txt'
word_count = count_words_in_file(file_path)
print(f"The file '{file_path}' contains {word_count} words.")

