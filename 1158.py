N,K = map(int,input().split())
p=[i for i in range(1,N+1)]
num=0
answer=[]
for i in range(N):
    num+=K-1
    if num >= len(p):
        num=num%len(p)
    answer.append(str(p.pop(num)))
print("<",", ".join(answer),">",sep='')