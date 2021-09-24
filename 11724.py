import sys
sys.setrecursionlimit(10000)
N,M=map(int,sys.stdin.readline().split())
link = [[] for i in range(N+1)]
visited = [False] * (N+1)
count=0

for i in range(M):
    u, v =  map(int, sys.stdin.readline().split())
    link[u].append(v)
    link[v].append(u)

def dfs(idx):
    visited[idx]=True
    for i in link[idx]:
        if not visited[i]:
            dfs(i)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1
print(count)