# Function to find row-wise sum of matrix elements
def row_wise_sum(mat, rows):
    print("\nRow-wise sums:")
    for i in range(rows):
        row_sum = sum(mat[i])
        print(f"Sum of row {i+1}: {row_sum}")

# Input size of matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter the elements row-wise:")
mat = []
for i in range(rows):
    row = list(map(int, input().split()))
    mat.append(row)

# Function call
row_wise_sum(mat, rows)
