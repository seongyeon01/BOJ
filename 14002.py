N=int(input())
A=list(map(int,input().split()))

dp=[1 for i in range(N)]
for i in range(1,N):
    for j in range(i):
        if A[j]<A[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

order = max(dp)
li = []
for i in range(N-1, -1, -1):
    if dp[i]==order:
        li.append(A[i])
        order-=1
li.reverse()
for i in li:
    print(i, end=' ')