N,M=map(int,input().split())
c=[]

def dfs(idx):
    if len(c)==M:
        print(' '.join(map(str, c)))
        return
    else:
        for i in range(idx,N+1):
            c.append(i)
            dfs(i)
            c.pop()

dfs(1)