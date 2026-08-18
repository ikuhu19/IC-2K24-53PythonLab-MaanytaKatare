# Aim: Number Guessing Game with bounded attempts and feedback.
import random

def guessing_game():
    target = random.randint(1, 100)
    max_attempts = 7
    print(f"I have picked a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
            
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number correctly in {attempt} attempts.")
            return
            
    print(f"Game Over! You ran out of attempts. The correct number was {target}.")

if __name__ == "__main__":
    guessing_game()