import re
pair2=re.compile('^[0-9]{17}(\d|X)$',re.I)
s=input()
if(pair2.match(s)):
    print("Yes")
else:
    print("No")