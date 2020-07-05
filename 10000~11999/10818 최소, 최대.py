number=int(input()) #N개 정수 입력
number_list=list(map(int, input().split())) #리스트에 정수 받기
print(number_list)
print(min(number_list),max(number_list)) #리스트에서 max min 함수 이용 추출

"""
number=int(input()) #N개 정수 입력
number_list=list(map(int, input().split())) #리스트에 정수 받기
number_list.sort() #리스트 순서대로 정렬
print(number_list[0],number_list[number-1]) #첫번째 정수 마지막 변수 출력

