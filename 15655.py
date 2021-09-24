from itertools import combinations
N,M=map(int,input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) 

for i in list(combinations(N_list, M)):
    for num in i:
        print(num, end=' ')
    print()