# Lab 1 - Python Basics

## 1. variable_practice.py
* **Aim:** Declare variables of different types and print their values and data types using `type()`.
* **Logic:** Variables are assigned string, integer, float, and boolean values. The `type()` function evaluates each variable's data type dynamically at runtime.
* **Sample Input / Output:**
  * *Input:* None (Hardcoded variables)
  * *Output:* `Variable: name | Value: Maanyta | Type: <class 'str'>`

## 2. greeting.py
* **Aim:** Take user name, age, and city as input and combine them into a formatted sentence.
* **Logic:** Uses Python's `input()` function to fetch user details as strings and interpolates them directly into an f-string template.
* **Sample Input / Output:**
  * *Input:* `Maanyta`, `20`, `Makroniya`
  * *Output:* `Hello Maanyta! You are 20 years old and live in Makroniya.`

## 3. arithmetic.py
* **Aim:** Compute basic arithmetic operations (sum, difference, product, quotient, remainder) on two numbers.
* **Logic:** Accepts two numeric inputs converted via `float()`, computes standard operators (`+`, `-`, `*`, `/`, `%`), and includes conditional logic to handle division by zero safely.
* **Sample Input / Output:**
  * *Input:* `10`, `3`
  * *Output:* `Sum: 13.0`, `Difference: 7.0`, `Product: 30.0`, `Quotient: 3.3333333333333335`, `Remainder: 1.0`

## 4. celsius_to_fahrenheit.py
* **Aim:** Convert user-inputted Celsius temperature into Fahrenheit.
* **Logic:** Applies the conversion formula $F = (C \times \frac{9}{5}) + 32$ on a float-casted temperature input.
* **Sample Input / Output:**
  * *Input:* `25`
  * *Output:* `25.0°C is equal to 77.0°F`

## 5. string_manipulation.py
* **Aim:** Perform multiple string manipulation methods on an input full name.
* **Logic:** Utilizes built-in string methods like `.upper()`, `.lower()`, `len()`, and slice notation `[::-1]` to reverse character sequences.
* **Sample Input / Output:**
  * *Input:* `Maanyta Katare`
  * *Output:* `Uppercase: MAANYTA KATARE`, `Reversed: erataK atynaaM`, `Length of name: 14`

## 6. escape_sequence.py
* **Aim:** Print a neatly formatted tabular receipt using formatting escape sequences.
* **Logic:** Combines `\t` (tabs) for column spacing and `\n` (newlines) to align structured text data.
* **Sample Input / Output:**
  * *Input:* None
  * *Output:* Clean table showing items, quantities, and prices aligned with tabs.

## 7. calculator.py (Optional)
* **Aim:** Provide a continuous loop menu-driven calculator supporting 4 primary arithmetic options.
* **Logic:** Employs a `while True` control loop, conditional branching (`if-elif-else`), and user break conditions to run calculations repeatedly until exit.
* **Sample Input / Output:**
  * *Input:* Choice `1`, Numbers `12` and `8`
  * *Output:* `Result: 20.0`