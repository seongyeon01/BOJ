T=int(input())
dp=[1,2,4]
for j in range(3,10):
    dp.append(dp[j-3]+dp[j-2]+dp[j-1])
for i in range(T):
    n=int(input())
    print(dp[n-1])