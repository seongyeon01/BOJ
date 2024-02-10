N = int(input())
X = list(map(int, input().split()))
X_sort = sorted(set(X))
X_dict = {}
for index, value in enumerate(X_sort):
    X_dict[value] = index
for i in X:
    print(X_dict[i], end = ' ')