year,month,date=eval(input())
if month in (1,3,5,7,8,10,12):
    day=31
else:
    if month in (4,6,9,11):
        day=30
    else:
        day=29 if year%4==0 and year%100!=0 or year%400==0 else 28
if date<day:
    tom=date+1
    y=year
    m=month
elif date==day:
     tom=1
     m=month+1 if month<12 else 1
     y=year+1 if month==12 else year
print(y,m,tom)