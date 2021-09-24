N=int(input())
M=int(input())
if M!=0:
    li=[str(i) for i in range(10)]
    num = list(map(int, input().split()))
    for i in num:
        li.remove(str(i))

answer=abs(100-N)

for a in range(1000001):
    a = str(a)
    for j in range(len(a)):
        if a[j] not in li:
            break
        elif j == (len(a) - 1):
            answer = min(answer, abs(N - int(a)) + len(str(a)))
print(answer)