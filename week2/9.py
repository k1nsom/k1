from math import fabs
from math import pi

def sin(x):
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return g
n=eval(input())
sum=0.0
for i in range(1,n+1):
    sum=sum+i*(1.0/n) *((2+1.0/n)**2+4*(2+1.0/n)*sin(2+1.0/n))
print(sum/n)