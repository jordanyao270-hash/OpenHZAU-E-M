d=input().strip()
s=eval(d)
d_new={}
for k in s.keys():
    if 'a'<=k<='z'and k.upper() in s:
        d_new[k.upper()]=s[k]+s[k.upper()]
    if 'a'<=k<='z'and k.upper() not in s:
        d_new[k.upper()]=s[k]
    if 'A'<=k<='Z'and k.lower() not in s:
        d_new[k]=s[k]

for k,v in d_new.items():
    print(k,v)