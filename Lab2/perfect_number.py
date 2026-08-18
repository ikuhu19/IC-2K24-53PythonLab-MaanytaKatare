# Aim: Check if a number is a perfect number and print all perfect numbers up to a limit.

def is_perfect(num):
    if num <= 0:
        return false if num < 0 else False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Single number check
try:
    n = int(input("Enter a number to check perfect number status: "))
    if is_perfect(n):
        print(f"{n} is a Perfect number.")
    else:
        print(f"{n} is not a Perfect number.")
except ValueError:
    print("Invalid input!")

# Limit range check
limit = int(input("\nEnter upper limit to find all perfect numbers: "))
print(f"Perfect numbers up to {limit}:")
for i in range(1, limit + 1):
    if is_perfect(i):
        print(i, end=" ")
print()