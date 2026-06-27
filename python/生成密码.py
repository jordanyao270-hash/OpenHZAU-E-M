import random
random.seed(10)
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length=int(input())
password=""
while len(password)<length:
    num=random.randint(0,len(s)-1)
    s2=s[num]
    if s2 not in password:
        password+=s2
print(password)
