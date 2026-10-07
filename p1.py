word = str(input("Enter a Word : "))

if (word == word[::-1]):
    print("The word is palindrome")
else:
    print("The word is not palindrome")