n=int(input())
m=list(map(int,input().split()))
k={}
a=[]
for i in range(1,len(m)-1):
    if m[i]<m[i-1] and m[i]<m[i+1]:
        k[i+1]='low'
        a.append(i)
    if m[i]>m[i-1] and m[i]>m[i+1]:
        k[i+1]='high'
        a.append(i)
print(len(a))
for q,i in k.items():
    print(q,i)
