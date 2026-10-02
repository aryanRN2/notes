# Code by Anushka

def euler(f, x0, y0, x_end, h=0.05):
    x = x0
    y = y0
    step = 0

    print(f"{'Step':<6}{'x':<10}{'y':<12}{'Slope':<12}")
    print("-" * 40)

    while x < x_end - 1e-9:
        slope = f(x, y)
        print(f"{step:<6}{x:<10.3f}{y:<12.5f}{slope:<12.5f}")
        y = y + h * slope
        x = x + h
        step = step + 1

    print(f"{step:<6}{x:<10.3f}{y:<12.5f}")
    return y


def f(x, y):
    return x + y


ans = euler(f, 0.0, 1.0, 0.2, h=0.05)
print(f"\ny(0.2): {ans:.5f}")
