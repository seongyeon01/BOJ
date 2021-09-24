N= list(input())
num = 0
stack = []

for i in range(len(N)):
    if N[i] == '(': 
        stack.append('(')
        
    else:
        if N[i-1] == '(': 
            stack.pop()
            num += len(stack)
            
        else:
            stack.pop() 
            num += 1 

print(num)