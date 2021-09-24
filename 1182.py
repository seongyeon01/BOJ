from itertools import combinations
N,S=map(int,input().split())
N_list=list(map(int, input().split()))

count=0

for i in range(1,N+1):
    a=combinations(N_list,i)
    for j in list(a):
        if sum(j)==S:
            count+=1

print(count)