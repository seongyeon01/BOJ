import sys
from collections import deque

N=int(sys.stdin.readline())
d=deque()

for i in range(N):
    word=sys.stdin.readline().split()
    order=word[0]

    if order=="push_front":
        d.appendleft(word[1])

    elif order=="push_back":
        d.append(word[1])

    elif order=="pop_front":
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())

    elif order=="pop_back":
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())

    elif order=="size":
        print(len(d))

    elif order =="empty":
        if len(d)==0:
            print(1)
        else:
            print(0)
            
    elif order=="front":
        if len(d)==0:
            print(-1)
        else:
            print(d[0])

    elif order=="back":
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])