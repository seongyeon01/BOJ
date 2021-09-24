N = int(input())
stack = list(input())
num=[]
result=[]
for i in range (N):
    num.append(int(input()))
for i in stack:
    if i.isalpha():
        result.append(num[ord(i)-ord('A')])
    else:
        a=result.pop()
        b=result.pop()
        if i=='+':
            result.append(b+a)
        elif i=='-':
            result.append(b-a)
        elif i=='*':
            result.append(b*a)
        elif i=='/':
            result.append(b/a)
print("%.2f"%(result[0]))            