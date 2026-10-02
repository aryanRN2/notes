# Code by Anushka

def newton_divided_diff(x, y, target_x):
    n = len(x)

    # Initialize 2D table with zeros using loops
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0.0)
        table.append(row)

    # First column is y values
    for i in range(n):
        table[i][0] = y[i]

    # Compute divided differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    print("Divided Difference Table:")
    for i in range(n):
        row_str = f"{x[i]:<6.1f}"
        for j in range(n - i):
            row_str += f"{table[i][j]:<12.4f}"
        print(row_str)

    # Evaluate the polynomial at target_x
    res = table[0][0]
    prod_term = 1.0
    for j in range(1, n):
        prod_term = prod_term * (target_x - x[j - 1])
        res += table[0][j] * prod_term

    return res


x_pts = [4.0, 5.0, 7.0, 10.0, 11.0]
y_pts = [48.0, 100.0, 294.0, 900.0, 1210.0]

ans = newton_divided_diff(x_pts, y_pts, 6.0)
print(f"\nInterpolated Value: {ans:.5f}")
