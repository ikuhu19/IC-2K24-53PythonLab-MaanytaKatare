# Aim: Check if a number is a palindrome using arithmetic operations, and check a string palindrome.

def is_number_palindrome(num):
    if num < 0:
        return False
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return original == rev

def is_string_palindrome(s):
    return s == s[::-1]

# Test numeric palindrome
n = int(input("Enter a number to check palindrome (arithmetic): "))
if is_number_palindrome(n):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")

# Test string palindrome
text = input("Enter a string to check palindrome: ")
if is_string_palindrome(text):
    print(f"'{text}' is a palindrome string.")
else:
    print(f"'{text}' is not a palindrome string.")