import  math
a=eval(input())
t=0
for i in range(2,a):
    if(a%i==0 or i*i>a):
        t=1
        break
if(t==1 or a<=1):
    print("不是质数")
else:
    print("是质数")