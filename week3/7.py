a=eval(input())
b=eval(input())
while(a%b):
    temp=a%b
    a=b
    b=temp
print(b)