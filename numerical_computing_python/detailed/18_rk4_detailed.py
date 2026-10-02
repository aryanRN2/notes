# Code by Anushka

def rk4(f, x0, y0, x_end, h=0.05):
    x = x0
    y = y0
    step = 0

    print(f"{'Step':<6}{'x':<8}{'y':<10}{'k1':<9}{'k2':<9}{'k3':<9}{'k4':<9}")
    print("-" * 60)

    while x < x_end - 1e-9:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2.0, y + k1 / 2.0)
        k3 = h * f(x + h / 2.0, y + k2 / 2.0)
        k4 = h * f(x + h, y + k3)
        print(f"{step:<6}{x:<8.2f}{y:<10.4f}{k1:<9.4f}{k2:<9.4f}{k3:<9.4f}{k4:<9.4f}")
        y = y + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        x = x + h
        step = step + 1

    print(f"{step:<6}{x:<8.2f}{y:<10.4f}")
    return y


def f(x, y):
    return x + y


ans = rk4(f, 0.0, 1.0, 0.2, h=0.05)
print(f"\ny(0.2): {ans:.5f}")
