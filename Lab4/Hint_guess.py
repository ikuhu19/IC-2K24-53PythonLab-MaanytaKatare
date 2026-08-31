import random

def run_hint_guessing():
    secret = random.randint(1, 100)
    score = 100
    attempts_left = 10
    
    print("I have picked a secret number between 1 and 100. You have 10 attempts.")
    
    while attempts_left > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if guess == secret:
            print(f"Correct! You won with a final score of {score}.")
            return
            
        score -= 10
        attempts_left -= 1
        
        if attempts_left == 0:
            print(f"You lost! The secret number was {secret}. Final score: 0.")
            break
            
        print("Wrong guess!")
        hint_even = "even" if secret % 2 == 0 else "odd"
        hint_five = "is" if secret % 5 == 0 else "is not"
        print(f"Hint: The number is {hint_even} and {hint_five} a multiple of 5.")
        print(f"Attempts remaining: {attempts_left} | Current Score: {score}")

if __name__ == "__main__":
    run_hint_guessing()