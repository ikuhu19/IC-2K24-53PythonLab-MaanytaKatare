# Aim: Build a small menu-driven calculator with at least 4 operations using a loop.
while True:
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            print("Result:", a / b if b != 0 else "Error: Division by zero")
    else:
        print("Invalid choice, please select between 1 and 5.")