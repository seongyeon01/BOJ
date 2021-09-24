T=int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    check = 1
    while(x <= M*N):
        if x%N == y%N:
            print(x)
            check = 0
            break
        x += M
    if check==1:
        print(-1)