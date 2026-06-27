def fac(s):
    q=1
    for i in range(1,s+1):
        q=q*i
    return q
n=int(input())
m=int(input())
c=fac(n)/fac(m)/fac(n-m)
d=round(c,1)
print('result:',d,sep="")