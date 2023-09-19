def nt(k, epsilon):
    guess = k/2
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess * guess) - k) / (guess * 2))
    return guess


print(nt(2, 0.000000001))
