N,M=map(int,input().split())
c=[]

def dfs():
    if len(c)==M:
        print(' '.join(map(str, c)))
        return
    else:
        for i in range(1,N+1):
            if i not in c:
                c.append(i)
                dfs()
                c.pop()

dfs()
