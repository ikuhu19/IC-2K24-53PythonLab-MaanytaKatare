Section A: Concept Check
1.When a menu-driven program needs to remember something across multiple choices in the same run (for example, an account balance), that value must be stored __outside_ the main loop, not inside it.
2.To generate a random number in Python, you first need to __import__the random module.
3.In a "computer guesses your number" game, the computer narrows its guesses using feedback from the user, which is the same principle as a __binary__ search.
4.If a withdrawal amount in an ATM simulation exceeds the current balance, the correct response is to ___reject___ the transaction and print an error, not to allow a negative balance.
5.A while loop condition that depends on a variable changed inside the loop (like attempts or balance) will only terminate if that variable is _update_ correctly on every iteration.

outside (You have to define the variable before the loop starts so it doesn't reset every time the loop repeats.)

import (You need to bring the module into your script first.)

binary (This is a classic search method where you cut the possibilities in half each time.)

reject (An ATM shouldn't give out money it doesn't have!)

updated (If you don't update the variable, the loop will run forever.)