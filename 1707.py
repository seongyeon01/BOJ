from collections import deque
import sys
K = int(sys.stdin.readline())
 
def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True
for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    isTrue = True
    s = [[] for i in range(V + 1)]
    bi = [0 for i in range(V + 1)]
    for j in range(E):
        a, b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)
    for K in range(1, V + 1):
        if bi[K] == 0:
            if not bfs(K):
                isTrue = False
                break
    print("YES" if isTrue else "NO")