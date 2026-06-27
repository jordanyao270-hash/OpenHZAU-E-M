st=input()
length=len(st)
flag=True
for i in range(length//2):
    if st[i]!=st[-i-1]:
        flag=False
        break
if flag:
    print('True')
else:
    print('False')
