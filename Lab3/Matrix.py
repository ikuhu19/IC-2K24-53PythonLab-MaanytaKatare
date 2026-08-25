print("Enter the 3x3 matrix row by row (space-separated):")
matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# 1. Display the matrix
print("\nMatrix:")
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# Trick: Put all the matrix numbers into one simple 1D list
all_numbers = []
for row in matrix:
    for num in row:
        all_numbers.append(num)

# 2 & 4. Use standard Python tools on our simple list
print(f"\nSum of all elements: {sum(all_numbers)}")
print(f"Largest element: {max(all_numbers)}")
print(f"Smallest element: {min(all_numbers)}")

# 3. Sum of main diagonal (where row and column index are the exact same)
diag_sum = 0
for i in range(3):
    diag_sum += matrix[i][i]
print(f"Sum of main diagonal: {diag_sum}")

# 5. Display the transpose (swap row and column)
print("\nTranspose of the matrix:")
for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()