a,b,c=eval(input())
ave=(a+b+c)/3
if ave>=90:
    print("first prize")
if 85<=ave<90:
    print("second prize")
if 80<=ave<85:
    print("third prize")
if ave<80:
    print("no prize")