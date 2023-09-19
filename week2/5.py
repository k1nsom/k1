def nt(k, epsilon):
    guess = k
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess * guess) - k) / (guess * 2))
    return guess

k=int(input())
print(nt(k, 0.000000001))
