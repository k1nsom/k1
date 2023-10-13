import random
import math

def monte_carlo_integration(f, a, b, n):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += f(x)
    average = total / n
    integral = average * (b - a)
    return integral

def f(x):
    return x**2 + 4 * x * math.sin(x)

a = 2
b = 3
n = 1000000

integral = monte_carlo_integration(f, a, b, n)
print("答案为:", integral)