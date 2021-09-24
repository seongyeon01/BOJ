N=int(input())
sum=0
for i in range(len(str(N))-1):
    sum+= 9 * (10 ** i) * (i + 1)
print(sum+(N-10**(len(str(N))-1)+1)*len(str(N)))