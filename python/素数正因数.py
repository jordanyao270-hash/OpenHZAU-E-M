n=int(input())
t=[]
if n<2:
    print("No Answer")
else:
    for i in range(2,n+1):
        if n%i==0:
            b=0
            for j in range(2,i):
                if i%j==0:
                    b+=1
            if b==0:
                t.append(i)
    if len(t)==0:
        print("No Answer")
    else:
        print(*t)

