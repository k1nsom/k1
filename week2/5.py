def nt(k, epsilon,b):
    guess = b
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess * guess) - k) / (guess * 2))
    return guess

k=int(input())
print(nt(k, 0.000000001,20))
print(nt(k, 0.000000001,2000))
print(nt(k, 0.000000001,2))
#精度变化，但相差不大。