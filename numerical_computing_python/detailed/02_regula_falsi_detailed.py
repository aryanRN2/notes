# Code by Anushka

def regula_falsi(f, a, b, tol=1e-5, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iter':<6}{'a':<12}{'b':<12}{'c (False)':<14}{'f(c)':<12}")
    print("-" * 56)

    c = a
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        print(f"{i:<6}{a:<12.5f}{b:<12.5f}{c:<14.5f}{fc:<12.5f}")

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    return c


def f(x):
    return x**3 - 2 * x - 5


root = regula_falsi(f, 2.0, 3.0)
print(f"\nRoot: {root:.5f}")
