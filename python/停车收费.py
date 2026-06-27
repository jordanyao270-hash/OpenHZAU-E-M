a=float(input("time:"))
if a<0.5:
    print("0")
elif 0.5<a<10:
    if int(a)!=a:
        b=(int(a)+1)*5
        print(b)
    else:
        b=int(a)*5
        print(b)
else:
    print("50")
