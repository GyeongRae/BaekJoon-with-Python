t = int(input())
data = []
for i in range(t):
    data.append(list(input().split()))
print(data)
data.sort(key = lambda x : int(x[0]))
for age, name in data:
    print(age, name)
