from collections import deque
n = int(input())
card = []
for i in range(1,n+1):
    card.append(i)
card=deque(card)
for j in range(n-1):
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0])
