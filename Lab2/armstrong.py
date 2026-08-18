# Aim: Check if a number is an Armstrong number and print all Armstrong numbers in a user-defined range.

def is_armstrong(num):
    if num < 0:
        return False
    str_num = str(num)
    power = len(str_num)
    total = sum(int(digit) ** power for digit in str_num)
    return total == num

# Single number check
try:
    n = int(input("Enter a number to check Armstrong status: "))
    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
except ValueError:
    print("Invalid input! Please enter an integer.")

# Range check
print("\n--- Armstrong Range Finder ---")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Armstrong numbers between {start} and {end}:")
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i, end=" ")
print()