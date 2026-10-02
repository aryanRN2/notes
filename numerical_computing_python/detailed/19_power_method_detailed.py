# Code by Anushka

def power_method(A, tol=1e-5, max_iter=50):
    n = len(A)
    x = []
    for _ in range(n):
        x.append(1.0)
    lambda_old = 0.0

    print(f"{'Iter':<6}{'Eigenvalue':<14}{'Eigenvector':<20}")
    print("-" * 40)

    for step in range(1, max_iter + 1):
        # Matrix-vector multiplication y = A * x
        y = []
        for i in range(n):
            row_sum = 0.0
            for j in range(n):
                row_sum += A[i][j] * x[j]
            y.append(row_sum)

        # Find maximum absolute value in y
        lambda_new = y[0]
        for val in y:
            if abs(val) > abs(lambda_new):
                lambda_new = val

        # Normalize eigenvector x = y / lambda_new
        for i in range(n):
            x[i] = y[i] / lambda_new

        vec_str = "["
        for i in range(n):
            vec_str += f"{x[i]:.3f}"
            if i < n - 1:
                vec_str += ", "
        vec_str += "]"

        print(f"{step:<6}{lambda_new:<14.4f}{vec_str:<20}")

        if abs(lambda_new - lambda_old) < tol:
            return lambda_new, x

        lambda_old = lambda_new

    return lambda_new, x


matrix = [
    [4.0, 1.0],
    [2.0, 3.0]
]

val, vec = power_method(matrix)
rounded_vec = []
for v in vec:
    rounded_vec.append(round(v, 4))
print(f"\nEigenvalue: {val:.4f}, Eigenvector: {rounded_vec}")
