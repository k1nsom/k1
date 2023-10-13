def nt(k, epsilon,b):
    guess = k/b
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess * guess) - k) / (guess * 2))
    return guess


print(nt(2, 0.000000001,2))
print(nt(2, 0.000000001,4))
print(nt(2, 0.000000001,8))
#精度变化，但大体差不多