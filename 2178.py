from collections import deque
import sys
N,M=map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

def search(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        dx=[+1,0,-1,0]
        dy=[0,+1,0,-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
      
            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
  
    return matrix[N-1][M-1]

print(search(0, 0))