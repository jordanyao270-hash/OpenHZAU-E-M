sex=input("Sex(F or M):")
age=input("Age(1-120):")
if sex=='F':
    if int(age)>=20:
        print("Yes")
    else:
        print("No")
elif sex=='M':
    if int(age)>=22:
        print("Yes")
    else:
        print("No")