h = []
for i in range(9):
    h.append(int(input()))
total = sum(h)
a = 0
b = 0
for i in range(8):
    for j in range(i + 1, 9):
        if total - (h[i] + h[j]) == 100:
            a = h[i]
            b = h[j]
h.remove(a)
h.remove(b)
h.sort()
for i in h:
    print(i)