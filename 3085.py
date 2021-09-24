N = int(input())

table = [list(map(str, input())) for i in range(N)]

result = 0

#문자를 바꿨을 때 가장 긴 연속한 부분 찾기
def check(table):
    count = 0
    for i in range(N):
        row = 1
        col = 1
        for j in range(N-1):
            #열순회
            if table[i][j] == table[i][j+1]:
                row += 1
            else:
                count = max(count, row)
                row = 1
            #행순회
            if table[j][i] == table[j+1][i]:
                col += 1
            else:
                count = max(count, col)
                col = 1
        count = max(count, row, col)
    return count

for i in range(N):
    for j in range(N-1):
        #열확인 -> 오른쪽에 다른문자가 있을때 바꾸고 최대길이인지 확인
        if table[i][j] != table[i][j+1]:
            temp = table[i][j]
            table[i][j] = table[i][j+1]
            table[i][j+1] = temp

            result = max(result, check(table))

            #다시 원래대로 되돌리기
            temp = table[i][j]
            table[i][j] = table[i][j+1]
            table[i][j+1] = temp
        #행확인
        if table[j][i] != table[j+1][i]:
            temp = table[j][i]
            table[j][i] = table[j+1][i]
            table[j+1][i] = temp

            result = max(result, check(table))
            #다시 원래대로 되돌리기
            temp = table[j][i]
            table[j][i] = table[j+1][i]
            table[j+1][i] = temp

print(result)