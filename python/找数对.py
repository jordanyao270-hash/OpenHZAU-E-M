a=list(map(int,input("numbers:").split(",")))
a.sort()
q=[]
for i in a:
    for j in a:
        if i+j==9 and (min(i,j),max(i,j)) not in q:
            q.append((min(i,j),max(i,j)))
print(q)


