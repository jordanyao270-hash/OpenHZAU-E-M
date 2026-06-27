#【问题描述】网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。以下是检查密码的标准：
#1. 至少有1个字母(大小写都至少有一个)
#2. 至少有1个数字
#3. 至少有1个字符（即非字母和非数字）
#4.最短交易密码长度：6
#5.交易密码的最大长度：12
psw=input()
f1=f2=f3=f4=0
if len(psw)<6 or len(psw)>12:
    print("False")
else:
    for i in psw:
        if "A"<=i.upper()<="Z":
            f1=1
        elif i in "1234567890":
            f2=1
        else:
            f3=1
    if f1+f2+f3==3:
        print("True")
    else:
        print("False")

