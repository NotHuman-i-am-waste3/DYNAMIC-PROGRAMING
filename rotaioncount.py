l=list(map(int,input().split()))
l1=list(map(int,input().split()))
for i in l1:
    if i>len(l):
        i=i%len(l)
    print(l[i:]+l[0:i])