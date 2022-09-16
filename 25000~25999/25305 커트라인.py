import sys
n,r = map(int,sys.stdin.readline().split())
l = list((map(int,sys.stdin.readline().split())))
l.sort()
print(l[len(l)-r])
