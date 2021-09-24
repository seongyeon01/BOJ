import sys

T=int(input())
case = [list(sys.stdin.readline().split()) for i in range(T)]
for i in range(T) :
    for j in case[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()
