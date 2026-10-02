# Code by Anushka

def newton_raphson(f, df, x0, tol=1e-5, max_iter=50):
    print(f"{'Iter':<6}{'x0':<12}{'f(x0)':<14}{'df(x0)':<14}{'x1':<12}")
    print("-" * 58)

    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Error: Derivative is zero.")
            return None

        x1 = x0 - (fx / dfx)
        print(f"{i:<6}{x0:<12.5f}{fx:<14.5f}{dfx:<14.5f}{x1:<12.5f}")

        if abs(x1 - x0) < tol or abs(f(x1)) < tol:
            return x1

        x0 = x1

    return x0


def f(x):
    return x**3 - 3 * x + 1


def df(x):
    return 3 * x**2 - 3


root = newton_raphson(f, df, 1.5)
print(f"\nRoot: {root:.5f}")
