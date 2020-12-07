c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    case = sum(n[1:])/n[0]
    count = 0
    for i in n[1:]:
        if(i > case):
                count += 1
    print(format(count/n[0], ".3%"))
