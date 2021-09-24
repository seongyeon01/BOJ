from itertools import combinations

L,C=map(int,input().split())

num=sorted(list(map(str,input().split())))

result=list(combinations(num,L))
for i in result:
    a=0
    b=0
    for j in range(L):
        if i[j] in ['a','e','i','o','u']:
            a+=1
        else:
            b+=1
    if a>=1 and b>=2:
        print(''.join(i))