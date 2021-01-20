n = int(input()) # 자연수 입력
ans = 0 #비교값 초기화
for i in range(1, n+1): # 1부터 자연수 +1 까지 범위를 탐색
    result = list(map(int, str(i))) # 자연수를 문자열로 잘라 배열 result 에 저장
    ans = i + sum(result) # 비교값을 sum 함수와 i 를 더 함

    if ans == n: # 값이 같다면 분해합이기 때문에 출력 그리고 1부터 탐색값이 증가하므로 가장 작은 생성자 고로 for문 정지
        print(i)
        break

    if i == n:
        print(0)
