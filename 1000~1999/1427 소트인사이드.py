n = input()
l = []
for i in range(len(n)):
    l.append(int(n[i:i+1]))
l.sort(reverse=True)
for j in range(len(l)):
    print(l[j],end='')
