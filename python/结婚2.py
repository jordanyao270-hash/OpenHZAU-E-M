sex=input("Sex(F or M):")
age=int(input("Age(1-120):"))
if sex not in ("F","M") or age<0 or age>120:
    print("Error")
else:
    if sex=="F":
        agelimit=20
    else:
        agelimit=22
    if age>=agelimit:
        print("Yes")
    else:
        print("No")
