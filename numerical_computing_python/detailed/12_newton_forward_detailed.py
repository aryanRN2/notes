# Code by Anushka

import math

def newton_forward(x, y, target_x):
    n = len(x)
    h = x[1] - x[0]
    u = (target_x - x[0]) / h

    # Initialize forward difference table using loops
    diff = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0.0)
        diff.append(row)

    # Row 0 contains y values
    for i in range(n):
        diff[0][i] = y[i]

    # Compute difference table
    for order in range(1, n):
        for i in range(n - order):
            diff[order][i] = diff[order - 1][i + 1] - diff[order - 1][i]

    print("Forward Difference Table:")
    for i in range(n):
        row_str = f"{x[i]:<6.1f}"
        for j in range(n - i):
            row_str += f"{diff[j][i]:<12.4f}"
        print(row_str)

    res = diff[0][0]
    u_term = 1.0
    for order in range(1, n):
        u_term = u_term * (u - (order - 1))
        res += (u_term * diff[order][0]) / math.factorial(order)

    return res


x_pts = [10.0, 20.0, 30.0, 40.0, 50.0]
y_pts = [0.1736, 0.3420, 0.5000, 0.6428, 0.7660]

ans = newton_forward(x_pts, y_pts, 15.0)
print(f"\nInterpolated Value: {ans:.5f}")
