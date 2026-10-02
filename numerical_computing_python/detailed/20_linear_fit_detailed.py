# Code by Anushka

def linear_fit(x, y):
    n = len(x)

    # Compute summations using loops
    sx = 0.0
    sy = 0.0
    sxy = 0.0
    sx2 = 0.0

    for i in range(n):
        sx += x[i]
        sy += y[i]
        sxy += x[i] * y[i]
        sx2 += x[i] ** 2

    print(f"n = {n}, sum_x = {sx:.2f}, sum_y = {sy:.2f}, sum_xy = {sxy:.2f}, sum_x2 = {sx2:.2f}")

    m = (n * sxy - sx * sy) / (n * sx2 - sx**2)
    c = (sy - m * sx) / float(n)
    return m, c


x_data = [1.0, 2.0, 3.0, 4.0, 5.0]
y_data = [2.2, 2.8, 3.6, 4.5, 5.1]

m, c = linear_fit(x_data, y_data)
print(f"Fitted Line: y = {m:.4f}x + {c:.4f}")
