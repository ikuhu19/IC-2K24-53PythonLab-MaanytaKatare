def run_reverse_guessing():
    low = 1
    high = 100
    guesses = 0
    
    print("Think of a number between 1 and 100!")
    
    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        
        print(f"\nMy guess is {guess}.")
        feedback = input("Is it 'high', 'low', or 'correct'? ").strip().lower()
        
        if feedback == 'correct':
            print(f"Yay! I found your number in {guesses} guesses.")
            break
        elif feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1
        else:
            print("Invalid input. Please type 'high', 'low', or 'correct'.")
            guesses -= 1 # Don't penalize for a typo

if __name__ == "__main__":
    run_reverse_guessing()