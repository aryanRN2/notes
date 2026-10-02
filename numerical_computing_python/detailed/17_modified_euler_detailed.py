# Code by Anushka

def modified_euler(f, x0, y0, x_end, h=0.05):
    x = x0
    y = y0
    step = 0

    print(f"{'Step':<6}{'x':<10}{'y':<12}{'y_predict':<14}")
    print("-" * 42)

    while x < x_end - 1e-9:
        k1 = f(x, y)
        y_predict = y + h * k1
        print(f"{step:<6}{x:<10.3f}{y:<12.5f}{y_predict:<14.5f}")
        k2 = f(x + h, y_predict)
        y = y + (h / 2.0) * (k1 + k2)
        x = x + h
        step = step + 1

    print(f"{step:<6}{x:<10.3f}{y:<12.5f}")
    return y


def f(x, y):
    return x + y


ans = modified_euler(f, 0.0, 1.0, 0.2, h=0.05)
print(f"\ny(0.2): {ans:.5f}")
