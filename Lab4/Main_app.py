import Atm
import Grade_calculator
import Hint_guess

def main_menu():
    while True:
        print("\n=== Main Application Menu ===")
        print("1. ATM Simulation")
        print("2. Student Grade Calculator")
        print("3. Guessing Game")
        print("4. Exit")
        
        choice = input("Select a program to run: ")
        
        if choice == '1':
            Atm.run_atm()
        elif choice == '2':
            Grade_calculator.run_grade_calculator()
        elif choice == '3':
            Hint_guess.run_hint_guessing()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main_menu()