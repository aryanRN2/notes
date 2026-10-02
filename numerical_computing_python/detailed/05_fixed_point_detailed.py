# Code by Anushka

import math

def fixed_point(g, x0, tol=1e-5, max_iter=50):
    print(f"{'Iter':<6}{'x0':<12}{'x1 = g(x0)':<16}{'Error':<12}")
    print("-" * 46)

    for i in range(1, max_iter + 1):
        x1 = g(x0)
        err = abs(x1 - x0)
        print(f"{i:<6}{x0:<12.5f}{x1:<16.5f}{err:<12.5f}")

        if err < tol:
            return x1

        x0 = x1

    return x0


def g(x):
    return math.cos(x)


root = fixed_point(g, 0.5)
print(f"\nFixed Point: {root:.5f}")
