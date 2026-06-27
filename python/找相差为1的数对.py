a=int(input())
b=list(map(int,input().split()))
r=[]
a=0
for i in b:
    if i+1 in b:
       if (i,i+1) not in r:
           r.append((i,i+1))
r.sort()
print(len(r))
for i in r:
    print(i[0],i[1])