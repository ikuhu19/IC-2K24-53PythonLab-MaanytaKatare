# Aim: Take name, age, and city as input and print a combined sentence using an f-string.
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Tricky logic: age is taken as string input, which works seamlessly inside f-strings.
print(f"Hello {name}! You are {0} years old and live in {city}.".format(age) if False else f"Hello {name}! You are {age} years old and live in {city}.")