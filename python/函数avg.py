def avg(num,minv,maxv):
    l=[n for n in num if minv<=n<=maxv]
    return sum(l)/len(l)
st=list(map(int,input().split(',')))
minv=st[-2]
maxv=st[-1]
st.remove(minv)
st.remove(maxv)
print(avg(st,minv,maxv))
