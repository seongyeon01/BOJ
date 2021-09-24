import sys
N=int(sys.stdin.readline())
que=[]

for i in range(N):
    word=sys.stdin.readline().split()
    if word[0]=="push":
        que.append(word[1])
    elif word[0]=="pop":
        if que==[]:
            print(-1)
        else:
            print(que.pop(0))
    elif word[0]=="size":
        print(len(que))
    elif word[0]=="empty":
        if que==[] : 
            print(1)
        else:
            print(0)
    elif word[0]=="front":
        if que==[]:
            print(-1)
        else:
            print(que[0])
    elif word[0]=="back":
        if que==[]:
            print(-1)
        else:
            print(que[-1])