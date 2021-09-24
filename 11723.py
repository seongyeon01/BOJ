import sys
M=int(sys.stdin.readline())
S=set()

for i in range(M):
    word=sys.stdin.readline().strip().split()
    if len(word)==1:
        if word[0]=="all":
            S=set([i for i in range(1,21)])
        else:
            S=set()
    else:
        x=int(word[1])
        if word[0]=="add":
            S.add(x)
        elif word[0]=="remove":
            S.discard(x)
        elif word[0]=="check":
            if x in S:
                print(1)
            else:
                print(0)
        elif word[0]=="toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(int(word[1]))