num = int(input())

numset = [None] * num

check = 0

numset = map(int, input().split())

numset = list(numset)

if(len(numset) == num): # 첫 입력 수와 리스트의 갯수가 일치할때만 작동
    for i in numset:
        count = 0
        for j in range(1, i+1): # 1부터 리스트 수 까지 전부 나누었다.
            if i % j ==0:
                count += 1
        if count == 2:
            check += 1

print(check)
