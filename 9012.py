T=int(input())

for i in range(T) :
    case = list(input())

    l_count=0
    r_count=0
    for j in case:
        if j=="(":
            l_count+=1
        elif j==")":
            r_count+=1
        if l_count < r_count:
            print('NO')
            break

    if l_count==r_count:
        print("YES")
    elif l_count > r_count:
        print("NO")
    