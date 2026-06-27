def isLeap(year):
    f=False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        f=True
    return f
def days(year,month):

    if month in (1, 3, 5, 7, 8, 10, 12):
        day = 31
    else:
        if month in (4, 6, 9, 11):
            day = 30
        else:
            day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    return day
l=list(map(int,input().split("/")))
y=l[0]
m=l[1]
d=l[2]
z=0
for i in range(1,m):
    z=z+days(y,i)
print(z+d)




