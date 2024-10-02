#Count a given letter in string
def count_letter(string, letter):
    return string.count(letter)

input_string = "Hello, how many times does the letter 'o' appear?"
letter_to_count = 'o'
count = count_letter(input_string, letter_to_count)
print(f"The letter '{letter_to_count}' appears {count} times in the string.")

