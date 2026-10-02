# Code by Anushka

def simpson_1_3(f, a, b, n=6):
    if n % 2 != 0:
        n += 1

    h = (b - a) / float(n)

    x_pts = []
    for i in range(n + 1):
        x_pts.append(a + i * h)

    y_pts = []
    for x in x_pts:
        y_pts.append(f(x))

    print(f"{'i':<6}{'x_i':<12}{'f(x_i)':<14}{'Mult':<6}")
    print("-" * 38)
    for i in range(len(x_pts)):
        if i == 0 or i == n:
            mult = 1
        elif i % 2 != 0:
            mult = 4
        else:
            mult = 2
        print(f"{i:<6}{x_pts[i]:<12.4f}{y_pts[i]:<14.5f}{mult:<6}")

    sum_odd = 0.0
    for i in range(1, n, 2):
        sum_odd += y_pts[i]

    sum_even = 0.0
    for i in range(2, n, 2):
        sum_even += y_pts[i]

    integral = (h / 3.0) * (y_pts[0] + y_pts[n] + 4.0 * sum_odd + 2.0 * sum_even)
    return integral


def f(x):
    return 1.0 / (1.0 + x**2)


ans = simpson_1_3(f, 0.0, 1.0, n=6)
print(f"\nIntegral: {ans:.5f}")
