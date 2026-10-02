# Code by Anushka

def trapezoidal(f, a, b, n=6):
    h = (b - a) / float(n)

    x_pts = []
    for i in range(n + 1):
        x_pts.append(a + i * h)

    y_pts = []
    for x in x_pts:
        y_pts.append(f(x))

    print(f"{'i':<6}{'x_i':<12}{'f(x_i)':<14}")
    print("-" * 32)
    for i in range(len(x_pts)):
        print(f"{i:<6}{x_pts[i]:<12.4f}{y_pts[i]:<14.5f}")

    sum_middle = 0.0
    for i in range(1, n):
        sum_middle += y_pts[i]

    integral = (h / 2.0) * (y_pts[0] + 2.0 * sum_middle + y_pts[n])
    return integral


def f(x):
    return 1.0 / (1.0 + x**2)


ans = trapezoidal(f, 0.0, 1.0, n=6)
print(f"\nIntegral: {ans:.5f}")
