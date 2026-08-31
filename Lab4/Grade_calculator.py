def get_grade(average):
    if average >= 90: return 'A'
    if average >= 75: return 'B'
    if average >= 60: return 'C'
    if average >= 40: return 'D'
    return 'F'

def run_grade_calculator():
    last_student = None
    
    while True:
        print("\n--- Grade Calculator ---")
        print("1. Enter marks | 2. View last student | 3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            try:
                marks = []
                for i in range(1, 6):
                    marks.append(float(input(f"Enter marks for subject {i}: ")))
                
                avg = sum(marks) / 5
                grade = get_grade(avg)
                last_student = {"average": avg, "grade": grade}
                print("Marks saved successfully!")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                
        elif choice == '2':
            if last_student:
                print(f"Last Student -> Average: {last_student['average']}, Grade: {last_student['grade']}")
            else:
                print("No student data entered yet.")
                
        elif choice == '3':
            print("Exiting Grade Calculator.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_grade_calculator()