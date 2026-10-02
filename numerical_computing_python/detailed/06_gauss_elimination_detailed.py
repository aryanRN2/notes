# Code by Anushka

def gauss_elimination(A, b):
    n = len(b)

    # Forward Elimination
    for i in range(n):
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]

    # Back Substitution
    x = []
    for _ in range(n):
        x.append(0.0)

    for i in range(n - 1, -1, -1):
        sum_ax = 0.0
        for j in range(i + 1, n):
            sum_ax = sum_ax + A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    return x


A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]
b = [8.0, -11.0, -3.0]

ans = gauss_elimination(A, b)
for i in range(len(ans)):
    print(f"x{i+1} = {ans[i]:.4f}")
