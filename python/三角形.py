a,b,c=eval(input("please input three numbers:"))
state="ordinary triangle"
f1=0
f2=0
if a<0 or b<0 or c<0:
    state="false"
else:
    if not a+b>c and a+c>b and b+c>a:
        state="false"
    else:
        if a==b==c:
            state="equilateral triangle"
        if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            state="right triangle"
print(state)