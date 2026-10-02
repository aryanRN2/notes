# Code by Anushka

def gauss_jacobi(A, b, tol=1e-5, max_iter=50):
    n = len(b)
    x = []
    for _ in range(n):
        x.append(0.0)

    # Print Table Header
    header = f"{'Iter':<6}"
    for i in range(n):
        header += f"{'x' + str(i+1):<12}"
    print(header)
    print("-" * (6 + 12 * n))

    for step in range(1, max_iter + 1):
        x_new = []
        for i in range(n):
            sum_other = 0.0
            for j in range(n):
                if j != i:
                    sum_other += A[i][j] * x[j]
            xi_val = (b[i] - sum_other) / A[i][i]
            x_new.append(xi_val)

        # Print current iteration values
        row_str = f"{step:<6}"
        for val in x_new:
            row_str += f"{val:<12.5f}"
        print(row_str)

        # Check convergence
        max_diff = 0.0
        for i in range(n):
            diff = abs(x_new[i] - x[i])
            if diff > max_diff:
                max_diff = diff

        if max_diff < tol:
            return x_new

        x = x_new

    return x


A = [
    [10.0, -1.0, 2.0],
    [-1.0, 11.0, -1.0],
    [2.0, -1.0, 10.0]
]
b = [6.0, 25.0, -11.0]

sol = gauss_jacobi(A, b)
rounded_sol = []
for v in sol:
    rounded_sol.append(round(v, 4))
print("\nSolution:", rounded_sol)
