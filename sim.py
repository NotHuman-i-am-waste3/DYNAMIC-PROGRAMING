def adi(a):
    l=[]
    g=a[0] ;h=a[0]
    for i in a[1:]:
        if i==g:
            h+=i
        else:
            l.append(len(h))
            h=i
        g=i
    if len(h)>0:
        l.append(len(h))
    return l
p=input().strip() 
s=input().split() 
d=adi(p) 
for i in s:
    if adi(i)==d:
        print(i,end=" ")