l = list(map(int, input().split()))
a = []
for i in range(1, len(l)):
    if l[i] > l[i-1]:
        a.append(l[i])
print(' '.join(map(str, a)))
