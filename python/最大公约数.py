m,n=eval(input())
if m<n:
    m,n=n,m
i=n
while not (m%i==0 and n%i==0):
    i=i-1
print(i)
