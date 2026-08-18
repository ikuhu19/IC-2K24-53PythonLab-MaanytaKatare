# Aim: Take a full name as input and apply at least three string methods.
full_name = input("Enter your full name: ")

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
# Tricky logic: String slicing [::-1] reverses the string sequence
print("Reversed:", full_name[::-1])
print("Length of name:", len(full_name))