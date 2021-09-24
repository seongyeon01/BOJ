import sys
sys.setrecursionlimit(5000000)

def search(i, j): # 탐색
    if 0<=i<h and 0<=j<w:
        if matrix[i][j]==1:
            matrix[i][j]=0

            search(i - 1, j - 1)
            search(i - 1, j)
            search(i - 1, j + 1)
            search(i, j - 1)
            search(i, j + 1)
            search(i + 1, j - 1)
            search(i + 1, j )
            search(i + 1, j + 1)
            return True
        return False

while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    land = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                search(i,j)
                land += 1
    
    print(land)