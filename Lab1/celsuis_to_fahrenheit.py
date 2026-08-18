# Aim: Convert temperature from Celsius to Fahrenheit using the standard formula.
celsius = float(input("Enter temperature in Celsius: "))

# Formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")