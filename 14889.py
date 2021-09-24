from itertools import combinations
N=int(input())
S=[]
members=[i for i in range(N)]

for i in range(N):
    S.append(list(map(int,input().split())))

#가능한 팀 조합 구하기
team=[]
for i in combinations(members,N//2):
    team.append(list(i))  

for i in range(len(team)//2):
    