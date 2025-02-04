# Check palindrom with manual reverse word
def check_palindrome(word):
    """
    The function `check_palindrome` in Python checks if a given word is a palindrome.
    
    :param word: The function `check_palindrome` takes a word as input and checks if it is a palindrome.
    A palindrome is a word that reads the same forwards and backwards
    :return: The function `check_palindrome` returns `True` if the input `word` is a palindrome (reads
    the same forwards and backwards), and `False` otherwise.
    """
    word = word.lower()
    i = len(word) - 1  
    reverse_word = ""
    while i >= 0:
        reverse_word += word[i]
        i -= 1

    if word == reverse_word:
        return True
    else:
        return False

print(check_palindrome("katak"))
print(check_palindrome("radar"))
print(check_palindrome("kasur"))

# check palindrom with reverse string use built in python function
def check_palindrome_2(word):
    word = word.lower()  
    reverse_word = word[::-1]

    if word == reverse_word:
        return True
    else:
        return False

print(check_palindrome_2("radar"))