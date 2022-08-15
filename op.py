r,c=map(int,input().split())
l=[ list(map(str,input().split())) for i in range(r) ]
a=0
def tree(z):
    ans=[]
    for i in range(0,len(z),3):
        p=z[i:i+3]
        for i in p:
            ans.append(int(''.join(i)))
        for i in list(zip(*p)):
            ans.append(int(''.join(i)))
        ans.append(int(''.join([p[0][0],p[1][1],p[2][2]])))
        ans.append(int(''.join([p[-1][-1],p[-2][-2],p[-3][-3]])))
    return(ans)
f=[]
m1,m2=[],[]
for i in range(0,c//3):
    z=[]
    for j in l:
        z+=[j[a:a+3]]
    print(z)
    f+=tree(z)
    a+=3
print(sorted(f))





