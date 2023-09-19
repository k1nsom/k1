n=int(input())
if((n-4)%3==0):
    print(int(4*3**((n-4)/3)))
elif((n-5)%3==0):
    print(int(6* 3 ** ((n - 5) / 3)))
elif (n% 3 == 0):
    print(int(3**(n/3)))