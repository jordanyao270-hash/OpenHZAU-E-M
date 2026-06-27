m=int(input())
n=0
y=0
while y<m:
    n=n+1
    y=y+1/(2*n-1)

yp=round(y-1/(2*n-1),2)
n=n-1
print("n=",n,",","y=",yp,sep="")

