num=input('')
b=num[6:14]
y=b[0:4]
m=b[4:6]
d=b[6:8]
s=int(num[-2])
print(y,'-',m,'-',d,sep='')
if s%2==0:
    print("F")
else:
    print("M")