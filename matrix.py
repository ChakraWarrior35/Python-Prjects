def check_matrix_type(mat, n):
    if all(mat[i][j] == mat[j][i] for i in range(n) for j in range(n)):
        return "Symmetric"
    elif all(mat[i][j] == -mat[j][i] for i in range(n) for j in range(n)):
        return "Skew-Symmetric"
    else:
        return "Neither"
n = int(input("Enter size of square matrix: "))
mat = []
print("Enter matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

print("Matrix type:", check_matrix_type(mat, n))
