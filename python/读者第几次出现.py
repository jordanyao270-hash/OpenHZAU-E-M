read=input().split()
a=[]
for i in range(len(read)):
    a.append(str(read[0:i+1].count(read[i])))
print(*a)
