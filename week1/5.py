l=[0,0,0,0]
for i in range(0,4):
  l[i]=input()
for i in range(0,4):
  for j in range(i,3):
    if(l[j]>l[j+1]):
      temp=l[j]
      l[j]=l[j+1]
      l[j+1]=temp
for i in range(0,4):
  print(l[i],end=' ')