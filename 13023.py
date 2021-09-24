N, M = map(int, input().split())
friend = [[] for i in range(N)]
visited = [False] * N

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(M):
    a, b =  map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
print(friend)

def dfs(idx, num):
    if num == 4:
        print(1)
        exit()
    for i in friend[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, num + 1)
            visited[i] = False

# 노드를 순서대로 방문하며 dfs를 수행합니다.
for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)