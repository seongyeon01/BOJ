from itertools import permutations
N=int(input())
N_list = list(map(int, input().split()))

K=[]
for i in range (1,N+1) :
    K.append(i)

M=list(permutations(K))

for i in range(len(N_list)):
    if N_list==list(M[-1]):
        print(-1)
        break
    elif N_list==list(M[i]):
        print(' '.join(map(str,M[i+1])))
        break