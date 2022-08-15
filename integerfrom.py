r,c=map(int,input().split())
R=r//3;C=c//3

#see screenshot(574) for question

l=[list(map(str,input().split())) for i in range(r)]
ans=[]
x=0;y=3
for k in range(R):
 p=0;q=3
 for j in range(C):
  o=[]
  for i in l[x:y]:
    o.append(i[p:q])
  p+=3
  q+=3
  ans+=[ int(''.join(i)) for i in o]
  ans+=[ int(''.join(i)) for i in zip(*o)]
  ans+=[int(''.join(o[0][0]+o[1][1]+o[2][2]))]+[int(''.join(o[0][-1]+o[1][-2]+o[2][-3]))]
 x+=3;y+=3
print(sorted(ans))
