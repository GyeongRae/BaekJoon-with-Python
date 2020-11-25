set = int(input())

for i in range(set):
    a = input()
    ans = list(a)
    count = 0
    case = 0
    for j in ans:
        if(j == 'O'):
            count += 1
            case += count
        elif(j == 'X'):
            count = 0
    print(case)

