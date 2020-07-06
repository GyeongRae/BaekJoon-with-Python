list1=[] #리스트 생성
i=0 #변수 초기화
while i<9: #9번 반복
    a=int(input()) #자연수 입력
    list1.append(a) #리스트에 변수 추가
    i+=1 #횟수 체크
num=max(list1) #max함수로 최대 크기 변수 찾기
print(num) 
print(list1.index(num)+1) #리스트는 0부터 시작하니 +1
