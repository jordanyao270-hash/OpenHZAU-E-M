def IsPrime(n):
    f=True
    for i in range(2,n):
        if n%i==0:
            f=False
            break
    return f
def Reverse(v):
    a=str(v)
    b=a[::-1]
    return int(b)
q=int(input())
l=[]
if q<=1:
    print("error")
else:
    for i in range(2,q+1):
        if IsPrime(i) and IsPrime(Reverse(i)):
            l.append(i)
    print(*l)


