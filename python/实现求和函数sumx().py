def sumx(*n):
    s=0
    for i in n:
        s=s+i
    return s
x,y=eval(input('>'))

print(sumx(x,y))

a,b,c=eval(input('>'))
q=sumx(a,b,c)
print(f"{q:.2f}")       #保留两位小数