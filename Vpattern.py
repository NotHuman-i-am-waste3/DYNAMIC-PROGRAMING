r,c=map(int,input().split())
l=[list(map(int,input().split()))  for _ in range(r)]
m=[list('*'*c) for i in range(r)]
a=c//2
for i in range(r-1,-1,-1):
    m[i][a]=l[i][a]
    m[i][-a-1]=l[i][-a-1]
    a-=1
    if a<0:
        break
for i in m:
    print(*i)