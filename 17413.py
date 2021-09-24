import sys

case = [list(sys.stdin.readline().split())]
for i in range(len(case)) :
    if case[i]=="<":
        i+=1
        while case[i]==">":
            i+=1
        i+=1
    for j in case[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()
