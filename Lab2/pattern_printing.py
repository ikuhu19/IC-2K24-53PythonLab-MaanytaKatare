# Aim: Print right-angled triangle, number pattern, and centered pyramid using nested loops.

rows = int(input("Enter number of rows (n): "))

print("\n1. Right-Angled Triangle of Stars:")
for i in range(1, rows + 1):
    print("*" * i)

print("\n2. Number Pattern (1 to row number):")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n3. Centered Pyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + " ".join(str(x) for x in range(1, i + 1)))