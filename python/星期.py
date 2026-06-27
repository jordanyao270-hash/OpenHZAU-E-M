day='MoTuWeThFrSaSu'
num=int(input())
d=day[num*2-2:num*2]
if num<8:
    print(d)
else:
    print('Err')