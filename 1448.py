N = int(input())
N_list = []
for i in range(N):
    N_list.append(int(input()))
N_list.sort(reverse=True)
for i in range(N-2):
    if ((N_list[i+2]+N_list[i+1])>N_list[i]) :
        print(N_list[i]+N_list[i+1]+N_list[i+2])
        break
else : 
    print(-1)