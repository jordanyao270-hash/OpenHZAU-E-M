n=input()
words=n.split()
max=''
for word in words:
    if len(word)>len(max):
        max=word
print(max)