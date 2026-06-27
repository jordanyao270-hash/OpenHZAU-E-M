num=input()
l=num.split()
a=set(l)
c={}
b=[]
for i in a:
    c[i]=l.count(i)
for k,v in c.items():
    if v==1:
        b.append(k)
print(*b)
