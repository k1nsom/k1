x=input()
y=input()
z=input()
if(z>x):
  temp=z
  z=x
  x=temp
if(z>y):
  temp=z
  z=y
  y=temp
if (y > x):
    temp = y
    y = x
    x = temp
print(z,y,x)
