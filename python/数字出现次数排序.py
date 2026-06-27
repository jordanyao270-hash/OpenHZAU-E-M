a=int(input())
b=list(map(int,input().split()))
r=set(b)
c={}
for i in r:
    c[i]=b.count(i)
q=sorted(c.items(), key=lambda x: (-x[1], x[0]))
for k,v in q:
    print(k,v)


