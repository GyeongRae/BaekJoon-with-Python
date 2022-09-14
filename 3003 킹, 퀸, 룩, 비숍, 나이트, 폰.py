lst = list(map(int, input().split()))
ori = [1,1,2,2,2,8]
for i in range(len(ori)):
    lst[i] = ori[i] - lst[i]
print(*lst)
