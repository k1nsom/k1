s=input()
t=1
temp=''
for i in s:
  if(i==temp):
    print("yes")
    t=0
    break
  temp=i
if(t==1):
  print("no")