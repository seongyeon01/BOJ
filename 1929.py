M,N=map(int,input().split())

def isprime(M, N):
    N += 1                            
    prime = [True] * N                
    for i in range(2, int(N**0.5)+1): 
        if prime[i]:                  
            for j in range(2*i, N, i):   
                prime[j] = False

    for i in range(M, N):
        if i > 1 and prime[i] == True:  
            print(i)

isprime(M, N)