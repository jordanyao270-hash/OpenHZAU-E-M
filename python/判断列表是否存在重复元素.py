def isRepeated(v):
    f=True
    if len(v) != len(set(v)):
        f=False
    return f
q=eval(input())
print("True" if not isRepeated(q) else "False")
