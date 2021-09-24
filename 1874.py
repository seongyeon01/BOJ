n=int(input())
count=0
stack=[]
result=[]
temp=True
for i in range(n):
    num=int(input())

    while count <num:
        count+=1
        stack.append(count)
        result.append("+")

    if stack[-1]==num:
        stack.pop()
        result.append("-")

    else:
        temp=False
if temp==False:
    print("NO")
else:
    print("\n".join(result))