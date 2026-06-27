def sumElem(n):
    h=0
    for i in range(1,n):
        if n%i==0:
            h+=i
    return h
a=int(input())
for i in range(1,a+1):
    if sumElem(sumElem(i))==i and sumElem(i)!=i and i<sumElem(i):
        print(i,sumElem(i),sep=" ")

