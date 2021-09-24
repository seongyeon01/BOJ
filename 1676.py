import math
N=int(input())
num=math.factorial(N)
result=0

while num%10 ==0:
    num//=10
    result+=1
print(result)