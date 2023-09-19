from math import  pi
print(pi)
def pi1(n):
    p = 10 ** (n + 10)
    a = p * 16 // 5
    b = p * 4 // -239
    f = a + b
    p = f
    j = 3
    while abs(f):
        a //= -25
        b //= -57121
        f = (a + b) // j
        p += f
        j += 2
    return p // 10**10
print(pi1(10))
pi2 = 0
N = eval(input())
for k in range(N):
    pi2 += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
print(pi2)