#15. Check whether a given word is palindrome or not

def is_palindrome(word):
    normalized_word = word.lower()
    return normalized_word == normalized_word[::-1]

word_to_check = "Racecar"
result = is_palindrome(word_to_check)
if result:
    print(f"'{word_to_check}' is a palindrome.")
else:
    print(f"'{word_to_check}' is not a palindrome.")
