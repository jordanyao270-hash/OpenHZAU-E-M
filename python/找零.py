mon=int(input())
mon2=100-mon
d=[50, 20, 10, 5, 2, 1]
count=0
for i in d:
    if mon2 == 0:
        break
    count += mon2 // i
    mon2 %= i

print(count)