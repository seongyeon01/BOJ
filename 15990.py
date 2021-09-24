T=int(input())
dp = [[0]*4 for i in range(100001)]

dp[1]=[0,1,0,0]
dp[2]=[0,0,1,0]
dp[3]=[0,1,1,1]

for i in range(4,100001):
    for j in range(1,4):
        dp[i][j]=sum(dp[i-j])%1000000009 -dp[i-j][j]
for i in range(T):
    n=int(input())
    print(sum(dp[n])%1000000009)