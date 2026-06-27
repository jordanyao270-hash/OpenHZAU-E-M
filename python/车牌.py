pat=int(input())
a=pat//1000
b=(pat//100)%10
c=(pat//10)%10
d=pat%10
if a==b and c==d and a!=c:
    a=pat**0.5
    if a**2==pat:
        print('Yes')
    else:
        print('No')
else:
    print('No')