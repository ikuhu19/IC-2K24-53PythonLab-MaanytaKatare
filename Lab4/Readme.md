1. ATM Simulation

Aim: Simulates basic ATM operations like deposits, withdrawals, and PIN checks.

Logic: Uses a continuous while loop to show a menu, updating a localized balance variable based on user input, and verifying withdrawal limits before subtracting.

Sample Input/Output:

Input: Withdraw 6000 (Current Balance: 5000).

Output: Error: Insufficient funds. Transaction rejected.

2. Student Grade Calculator

Aim: Calculates the average of 5 subjects and assigns a letter grade.

Logic: Loops 5 times to collect floats into a list, calculates the average using sum(), maps it to a grade via standard if/elif logic, and stores the result in a dictionary.

Sample Input/Output:

Input: 85, 92, 78, 60, 55.

Output: Average: 74.0, Grade: C. (Inputting 'abc' triggers an "Invalid input!" message).

3. Reverse Guessing Game

Aim: The computer guesses the user's secret number efficiently.

Logic: Implements a binary search algorithm. It tracks a low and high bound, guessing the exact midpoint (low + high) // 2 each time until the user confirms it's correct.

Sample Input/Output:

Secret Number: 37.

Output: Guesses 50 (User: low) -> Guesses 25 (User: high) -> Guesses 37 (User: correct).

4. Guessing Game with Hints

Aim: A number guessing game where the player gets scoring and mathematical hints.

Logic: Uses the random module to pick a target. A while loop tracks attempts (max 10) and score. The modulo operator % checks for even/odd and divisibility by 5 to generate hints.

Sample Input/Output:

Secret Number: 20. Input Guess: 15.

Output: Wrong guess! Hint: The number is even and is a multiple of 5. Attempts remaining: 9 | Current Score: 90.