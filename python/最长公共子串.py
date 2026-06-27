#【问题描述】编写一个函数 longest_substring(s1, s2)，它接收两个字符串 s1 和 s2 作为输入，要求返回两个字符串的最长公共子串。如果有多个最长公共子串，返回其中任意一个即可。如果没有公共子串，返回空字符串。
#程序中输入两个串，调用函数求最长子串，如果有显示该串，如何没有则打印“no find”。
#【样例输入】
#s1:abcdefg
#s2:xyzabcdf
#【样例输出】
#abcd
def zi(s):
    z=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            z.append(s[i:j])
    return z
def longest_substring(s1, s2):
    substrings_s1 = zi(s1)
    common_substrings = [sub for sub in substrings_s1 if sub in s2]
    if not common_substrings:
        return ""
    return max(common_substrings, key=len)


s1 = input()
s2 = input()

result = longest_substring(s1, s2)
if len(result)>1:
    print(result)
else:
    print("no find")