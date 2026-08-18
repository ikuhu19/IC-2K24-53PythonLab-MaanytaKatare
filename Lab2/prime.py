# Aim: Check if a number is prime and print all prime numbers up to a given limit.

def is_prime(num):
    if num <= 1:
        return False
    # Logic: Only check divisors up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Single number check
try:
    n = int(input("Enter a number to check prime status: "))
    if is_prime(n):
        print(f"{n} is a Prime number.")
    else:
        print(f"{n} is not a Prime number.")
except ValueError:
    print("Invalid input!")

# Limit range check
limit = int(input("\nEnter upper limit to find all prime numbers: "))
print(f"Prime numbers up to {limit}:")
for i in range(2, limit + 1):
    if is_prime(i):
        print(i, end=" ")
print()