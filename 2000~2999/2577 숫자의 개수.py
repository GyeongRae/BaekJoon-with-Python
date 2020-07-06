nA = int(input())
nB = int(input())
nC = int(input())

sResult = str(nA*nB*nC) # 이 시점에서 sResult는 "17037300" 이 돼
arCount = [0 for i in range(10)] # 이걸 리스트 컴프리헨션이라고 불러 아마 블로그에 내가 써놨을거야


for c in sResult:
    arCount[int(c)] += 1


for element in arCount:
    print(element)
    
