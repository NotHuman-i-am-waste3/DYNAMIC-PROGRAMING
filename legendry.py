r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
l=['0'+str(i) for i in range(c)]+[str(i)+str(c-1) for i in range(1,r)]+[str(r-1)+str(i) for i in range(1,c-1)][::-1]+[(str(i)+'0') for i in range(1,r)][::-1]
l=[l[-1]]+l
L=[]
for i in range(len(l)):
    a=int(l[i][0]);b=int(l[i][1])
    L.append(int(str(m[a][b])[::-1]))
for i in range(1,len(l)):
    a=int(l[i][0]);b=int(l[i][1])
    c=int(l[i-1][0]);d=int(l[i-1][1])
    m[a][b]=L[i-1]
for i in m:
    print(*i)




# 00 01 02 03 04
# 10          14        
# 20          24
# 30 31 32 33 34
# 40 41 42 43 44