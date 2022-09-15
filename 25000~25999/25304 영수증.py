topr = int(input())
ton = int(input())
sum = 0
for i in range(ton):
    a,b = map(int,input().split())
    sum += a*b

if(topr == sum):
    print("Yes")
else:
    print("No")
