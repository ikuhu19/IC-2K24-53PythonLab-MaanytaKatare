# Aim: Take two numbers as input and print sum, difference, product, quotient, and remainder.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
# Tricky logic: Checking for zero division to prevent runtime errors
if num2 != 0:
    print("Quotient:", num1 / num2)
    print("Remainder:", num1 % num2)
else:
    print("Quotient: Undefined (division by zero)")
    print("Remainder: Undefined")