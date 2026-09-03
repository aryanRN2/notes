#!/usr/bin/env python3
from typing import Callable, Optional


def newton_raphson(
    f: Callable[[float], float],
    fp: Callable[[float], float],
    x0: float,
    tol: float = 1e-8,
    max_iter: int = 100,
) -> Optional[float]:
    x = x0
    iteration_log = []
    for i in range(1, max_iter + 1):
        fx = f(x)
        fpx = fp(x)
        iteration_log.append((i, x, fx))

        if fpx == 0:
            print(f"[Iter {i}] Zero derivative encountered – aborting.")
            break

        if abs(fx) < tol:
            print(f"[Iter {i}] Converged: f({x}) = {fx:.2e}")
            break

        x = x - fx / fpx
    else:
        print("Maximum iterations reached without convergence.")

    print("\nFull iteration log:")
    for i, xi, fxi in iteration_log:
        print(f"Iter {i}: x = {xi:.10f}, f(x) = {fxi:.10e}")

    return x if iteration_log else None


if __name__ == "__main__":
    def f(x: float) -> float:
        return x**3 - x - 2

    def fp(x: float) -> float:
        return 3 * x**2 - 1

    while True:
        try:
            interval = input("Enter lower and upper bounds (a b): ").strip().split()
            if len(interval) != 2:
                raise ValueError("Please provide exactly two numbers.")
            a, b = map(float, interval)
            if a >= b:
                raise ValueError("Lower bound must be less than upper bound.")
            if f(a) * f(b) >= 0:
                raise ValueError("Function does not change sign on [a, b]; cannot guarantee a root.")
            break
        except Exception as e:
            print(f"Invalid interval input: {e}. Please try again.")

    try:
        max_iter_input = input("Enter maximum iterations (default 100): ").strip()
        max_iter = int(max_iter_input) if max_iter_input else 100
        if max_iter <= 0:
            raise ValueError("Iterations must be positive.")
    except Exception as e:
        print(f"Invalid iteration input: {e}. Using default 100.")
        max_iter = 100

    try:
        tol_input = input("Enter tolerance (default 1e-8): ").strip()
        tol = float(tol_input) if tol_input else 1e-8
        if tol <= 0:
            raise ValueError("Tolerance must be positive.")
        if tol > 1e-2:
            print(f"Tolerance {tol} is too large; using default 1e-8.")
            tol = 1e-8
    except Exception as e:
        print(f"Invalid tolerance input: {e}. Using default 1e-8.")
        tol = 1e-8

    x0 = (a + b) / 2.0
    print(f"Starting Newton‑Raphson with initial guess x0 = {x0:.6f}\n")

    root = newton_raphson(f, fp, x0=x0, tol=tol, max_iter=max_iter)
    if root is not None:
        print(f"Root ≈ {root:.10f}")
