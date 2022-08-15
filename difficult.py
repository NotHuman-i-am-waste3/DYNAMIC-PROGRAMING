
m,n=map(int,input().split())
l=list(map(int,input().split()));L=[]
for i in range(len(l)+1):
     for j in range(i+1,len(l)+1): 
        if len(l[i:j])==n and set(l[i:j])=={1}: 
            L.append(j)
print(L)
p=[ L[i] if L[i]%n==0 else L[i] if L[i+1]-L[i]!=1 else '' for i in range(len(L)-2)]
if '' in p:
  p.remove('')
if len(L)>2:
 if L[-2]%n==0:
     p.append(L[-2]) 
 elif L[-2]-L[-3]!=1:
        p.append(L[-2])
 if L[-1]%n==0:
     p.append(L[-1]) 
 elif L[-1]-L[-2]!=1:
        p.append(L[-1])
L=p
for i in range(len(L)):
     l.insert(L[i]+i,0)
if set(l[-n:])=={1}:
    for i in l+[0]:
        print(i,end=' ')
else:
   for i in l:
        print(i,end=' ')
