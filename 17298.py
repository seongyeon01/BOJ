import sys
N=int(input())
stack = list(sys.stdin.readline().split())

for i in range (N):
    j=i+1
    for j in range (N):
        if stack[j]>stack[i]:
            print(stack[j])
            break
        else:
            print(-1)
            break

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)