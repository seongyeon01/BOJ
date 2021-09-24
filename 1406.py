import sys
N=list(sys.stdin.readline().strip())
M=int(sys.stdin.readline())
a=[]

for i in range(M):
    word=sys.stdin.readline().strip()
    if word[0]=="P":
        N.append(word[2])
    elif word[0]=="L" and N!=[]:
        a.append(N.pop())
    elif word[0]=="D" and a!=[]:
        N.append(a.pop())        
    elif word[0]=="B" and N!=[]:
        N.pop()

print("".join(N+list(reversed(a))))