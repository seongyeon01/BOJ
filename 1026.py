N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum = 0
A.sort()
B.sort()
for i in range(N):
    sum += (A[i]*B[-(i+1)])
print(sum)