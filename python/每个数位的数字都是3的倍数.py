a,b=eval(input())
l=[num for num in range(a,b+1)]
nl=[]
for num in l:
    st=str(num)
    f=all(int(ch)%3==0 for ch in st)
    if f:
        nl.append(num)
if nl==[]:
    print("no find")
else:
    print(*nl,sep=",")
