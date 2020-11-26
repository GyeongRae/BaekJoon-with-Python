n, m=map(int, input().split())
num=list(map(int, input().split()))
answer = 0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1, n):
                
                if(num[i]+num[j]+num[k]>m):
                    continue
                else:
                    answer= max(answer,num[i]+num[j]+num[k])
print(answer)
