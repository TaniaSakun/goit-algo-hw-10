import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import scipy.integrate as spi


def f(x):
    return x**3 + x**2 + x + 3


def calc(f, a, b):
    res, _ = spi.quad(f, a, b)
    return res


def calculate_monte_carlo(f, a, b):
    y_max = f(b)
    points = [(random.uniform(a, b), random.uniform(0, y_max)) for _ in range(10000)]
    hit_points = [p for p in points if p[1] <= f(p[0])]
    M = len(hit_points)
    N = len(points)
    return (M / N) * ((b - a) * y_max)


def draw_function(f, a, b):
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("f(x) = x^2 + 1  [0..2]")
    plt.grid()
    plt.show()


def monte_carlo_calculation_task():
    a = 0
    b = 2

    print("SciPy quad calculation: ", calc(f, a, b))
    print("Monte Carlo calculation:", calculate_monte_carlo(f, a, b))
    draw_function(f, a, b)
