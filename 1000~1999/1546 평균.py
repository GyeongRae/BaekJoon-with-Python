n=int(input())
fnum=0
num_list = list(map(float, input().split()))
num=max(num_list)
for i in range(n):
    num_list[i]=num_list[i]/num*100
    fnum+=num_list[i]
print(round(fnum/n,2))
