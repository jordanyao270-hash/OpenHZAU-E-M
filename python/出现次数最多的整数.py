a=list(map(int,input().split()))
r=set(a)
q=list(r)
q.sort()
c={}
b=[]
for i in q:
    c[i]=a.count(i)
    b.append(a.count(i))
b.sort()
e=max(b)
for k,v in c.items():
    if v==e:
        print(k,v)

