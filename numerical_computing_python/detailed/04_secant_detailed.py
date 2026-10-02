# Code by Anushka

def secant(f, x0, x1, tol=1e-5, max_iter=50):
    print(f"{'Iter':<6}{'x0':<12}{'x1':<12}{'x2':<14}{'f(x2)':<12}")
    print("-" * 56)

    for i in range(1, max_iter + 1):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("Error: Division by zero in Secant formula.")
            return None

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        print(f"{i:<6}{x0:<12.5f}{x1:<12.5f}{x2:<14.5f}{f2:<12.5f}")

        if abs(x2 - x1) < tol or abs(f2) < tol:
            return x2

        x0 = x1
        x1 = x2

    return x1


def f(x):
    return x**2 - 4


root = secant(f, 1.0, 3.0)
print(f"\nRoot: {root:.5f}")
