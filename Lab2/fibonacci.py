# Aim: Print first n terms of Fibonacci series using a loop and compare with a recursive version tracking calls.

# Global counter to track recursive function calls
call_count = 0

def fibonacci_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Loop version
n_terms = int(input("Enter number of terms for Fibonacci series: "))
if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series (Loop version):")
    a, b = 0, 1
    for _ in range(n_terms):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Small recursive test to demonstrate work growth
small_n = 10
call_count = 0
fibonacci_recursive(small_n)
print(f"Recursive Fibonacci for n = {small_n} made {call_count} function calls.")