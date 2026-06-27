psw=input()
flag=True
for ch in psw:
    if ch not in '0123456789':
        flag=False
        break
if not flag:
    print("wrong")
else:
    f=1
    for i in range(0,6):
        if (int(psw[i])+1)**3%10!=int(psw[i+1]):
         f=0
        break
    if f==1:
        print("right")
    else:
        print("wrong")