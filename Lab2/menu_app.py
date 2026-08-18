# Aim: Combine programs 1 to 6 into a single robust menu-driven application.
import armstrong, prime, perfect_number, palindrome, fibonacci, pattern_printing

def main():
    while True:
        print("\n===== LAB 2 MENU-DRIVEN APPLICATION =====")
        print("1. Check Armstrong Number")
        print("2. Check Prime Number")
        print("3. Check Perfect Number")
        print("4. Check Palindrome (Number & String)")
        print("5. Fibonacci Series")
        print("6. Pattern Printing")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")
        
        if choice == '1':
            n = int(input("Enter number: "))
            print("Is Armstrong:", armstrong.is_armstrong(n))
        elif choice == '2':
            n = int(input("Enter number: "))
            print("Is Prime:", prime.is_prime(n))
        elif choice == '3':
            n = int(input("Enter number: "))
            print("Is Perfect:", perfect_number.is_perfect(n))
        elif choice == '4':
            n = int(input("Enter number for palindrome: "))
            print("Is Number Palindrome:", palindrome.is_number_palindrome(n))
        elif choice == '5':
            terms = int(input("Enter terms: "))
            a, b = 0, 1
            for _ in range(terms):
                print(a, end=" ")
                a, b = b, a + b
            print()
        elif choice == '6':
            r = int(input("Enter rows: "))
            for i in range(1, r + 1):
                print("*" * i)
        elif choice == '7':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection! Please choose between 1 and 7.")

if __name__ == "__main__":
    main()