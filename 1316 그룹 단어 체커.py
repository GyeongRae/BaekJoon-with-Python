n = int(input())
c = n
for i in range(n):
    word = list(input())
    for j in range(0,len(word)-1):
        if(word[j] == word[j+1]):
            continue
        if  (word[j] in word[j+1:]):
            c -= 1
            break
print(c)
