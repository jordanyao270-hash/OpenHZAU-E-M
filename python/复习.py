#import random
#a=input('name')
#random.seed(10)
#b=random.randint(0,9)
#print(a,', Your lucky number is ',b,'.',sep=' )


#num=input('')
#b=num[6:14]
#y=b[0:4]
#m=b[4:6]
#d=b[6:8]
#s=int(num[-2])
#print(y,'-',m,'-',d,sep='')
#if s%2==0:
#    print("F")
#else:
#    print("M")


#num=input()
#d=num[::-1]
#if d==num:
#    print("True")
#else:
#    print("False")


#n=112
#if n%2==0:
#    print("even")
#else:
#    print("odd")


#a=input()
#b=a[::-1]
#print(int(b))


#num=int(input())
#month="JanFebMarAprMayJunJulAugSepOctNovDec"
#re=month[num*3-3:num*3]
#if num>12 or num<1:
#    print("Err")
#else:
#    print(re)


#a=input()
#b=input()
#w=a*6
#r=b*3
#print(w,'-',r,sep='')


#a=input()
#b=input()
#w=a*6
#r=b*3
#q=int(w)-int(r)
#print(q)


#a=input()
#b=int(a)**0.5
#if a[0]==a[1] and a[2]==a[3] and a[1]!=a[2] and b**2==int(a):
#    print("yes")
#else:
#    print("no")


#def IsPrime(n)
#    for n in range(2, n):
#        if n % 2 == 0:
#            f=False
#            break
#    return f
#def Reverse(v)
#    a=str(v)
#    b=a[::-1]
#    return int(b)
#a=int(input())
#b=[]
#if a<=1:
#    print("error")
#else:
#    for i in range(2,a+1):
#        if IsPrime(i) and IsPrime(Reverse(i)):
#            b.append(i)
#    print(*b)


#def isRepeated(v):
#    f=True
#    if len(v)!=len(set(v)):
#        f=False
#    return f
#a=eval(input())
#if isRepeated(a)==True:
#    print("True")
#    else:
#    print("False")


#def sumElem(a):
#    d=0
#    for i in (0,a+1):
#        if a%i==0:
#            d+=i
#    return d
#a=int(input())
#for i in range(1,a+1):
#    if sumElem(sumElem(i))==i and sumElem(i)!=i and sumElem(i)>i:
#        print(i,sumElem(i),sep=" ")


#def avg(num,minv,maxv):
#    l=[n for n in num if minv<=n<=maxv]
#    return sum(l)/len(l)
#st=list(map(int,input().split(",")))
#minv=st[-2]
#maxv=st[-1]
#st.remove(minv)
#st.remove(maxv)
#print(avg(st,minv,maxv))


#def sumx(*x)
#    x=0
#    for i in x:
#        x+=i
#    return x
#x,y=eval(input('>'))
#print(sumx(x,y))
#a,b,c=eval(input('>'))
#q=sumx(a,b,c)
#print(f"{q:.2f}")


#def isLeap(year):
#    f=False
#    if year%4==0 and year%100!=0 or year%400==0:
#        f=True
#    return f
#def days(year,month):
#    if month in (1, 3, 5, 7, 8, 10, 12):
#        day=31
#    else:
#        if month in (4,6,9,11):
#            day=30
#        else:
#            day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#    return day
#date=list(map(int,input().split("/")))
#year=date[0]
#month=date[1]
#day=date[2]
#for i in range(1,month):
#    day+=days(year,i)
#print(day)


#def longest_substring(s1, s2):



