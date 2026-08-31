Section B: Trace the Logic (do on paper first)
1. An ATM simulation starts with a balance of 5000. The user does the following in order: checks balance, withdraws 2000, deposits 500, withdraws 4000. Trace each step and write the balance after each operation, and note which operation (if any) should be rejected and why.
Ans1. ATM Simulation Trace

Start: Initial balance is 5000.

Step 1 (Check balance): Balance remains 5000.

Step 2 (Withdraw 2000): 5000 - 2000 = 3000. New balance is 3000.

Step 3 (Deposit 500): 3000 + 500 = 3500. New balance is 3500.

Step 4 (Withdraw 4000): Rejected. The requested withdrawal (4000) is greater than the available balance (3500). The balance remains 3500.

2.In a "computer guesses your number" game with range 1 to 100, the user has secretly picked 37. The computer's strategy is to always guess the midpoint of the current possible range. Trace the computer's first four guesses and the user's feedback (too high / too low / correct) at each step, the same way binary search narrows down a range.
Ans2. Reverse Guessing Game Trace (Target = 37)

Guess 1: Midpoint of 1 and 100 is (1 + 100) // 2 = 50.

User Feedback: Too high.

Guess 2: Midpoint of 1 and 49 is (1 + 49) // 2 = 25.

User Feedback: Too low.

Guess 3: Midpoint of 26 and 49 is (26 + 49) // 2 = 37.

User Feedback: Correct!

3. A student's grade calculator takes marks in 5 subjects and assigns a grade based on the average: 90 and above is A, 75 to 89 is B, 60 to 74 is C, 40 to 59 is D, below 40 is F. For marks 85, 92, 78, 60, 55, compute the average by hand and determine the grade.
Ans3. Grade Calculator Trace

Marks to add: 85 + 92 + 78 + 60 + 55 = 370

Compute average: 370 / 5 = 74

Determine grade: The score of 74 falls exactly into the "60 to 74 is C" bracket.

Final Grade: C
