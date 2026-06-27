mon='JanFebMarAprMayJunErrAugSepOctNovDec'
num=int(input())
b=mon[num*3-3:num*3]
if num<13:
    print(b)
else:
    print('Err')