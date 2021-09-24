N,M,V=map(int,input().split())

graph=[[0]*(N+1) for i in range(N+1)]
visited=[False]*(N+1)

for i in range(M):
    a, b =  map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1

def dfs(V):
    print(V,end=' ')
    visited[V]=True
    for i in range(1,N+1):
        if visited[i]==False and graph[V][i]==1:
            dfs(i)

def bfs(V):
    visited=[False]*(N+1)
    queue=[V]
    while(queue):
        visited[V]=True
        V=queue[0]
        print(V,end=' ')
        del queue[0]
        for i in range(1,N+1):
            if visited[i]==False and graph[V][i]==1:
                queue.append(i)
                visited[i]=True
dfs(V)
print()
bfs(V)