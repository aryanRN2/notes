# Code by Anushka

def gauss_jordan(A, b):
    n = len(b)

    for i in range(n):
        pivot = A[i][i]

        # Normalize the pivot row
        for j in range(n):
            A[i][j] = A[i][j] / pivot
        b[i] = b[i] / pivot

        # Eliminate all other rows
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] = A[k][j] - factor * A[i][j]
                b[k] = b[k] - factor * b[i]

    return b


A = [
    [2.0, 3.0, 1.0],
    [1.0, 2.0, 3.0],
    [3.0, 1.0, 2.0]
]
b = [9.0, 6.0, 8.0]

ans = gauss_jordan(A, b)
for i in range(len(ans)):
    print(f"x{i+1} = {ans[i]:.4f}")
