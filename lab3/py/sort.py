l = [9,5,2,8,3,1,7,3]
N = len(l)

for i in range(N - 1):
    min = i
    for j in range(i + 1, N):
        if l[min] > l[j]: min = j
    l[i], l[min] = l[min], l[i]
print('排序后：')
for i in range(N):
    print(l[i])