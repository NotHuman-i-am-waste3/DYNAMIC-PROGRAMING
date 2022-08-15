n=int(input())
m=n//2
L=[]
for i in range(1,m+2):
    l=''
    for j in range(i):
        if j%2==0:
            l=l+'*'
        else:
            l=l+'-'
    L.append(l[::-1])
L=L+L[0:-1][::-1]
for i in L:
    print(i)

