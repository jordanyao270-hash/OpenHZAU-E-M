psw=input()
f1=f2=f3=0
if not(6<=len(psw)<=12):
    print("False")
else:
    for i in psw:
        if "A"<=i.upper()<="Z":
            f1=1
        if "0"<=i<="9":
            f2=1
        if i in "!@#$%^&*<>?":
            f3=1
    if f1+f2+f3==3:
        print("True")
    else:
        print("False")