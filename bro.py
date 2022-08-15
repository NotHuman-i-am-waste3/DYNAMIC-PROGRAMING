n=int(input());l=[]
for i in range(n):
    s=input().strip() 
    l.append(s)
for i in range(len(l)):
    c=0 ;k=l[i]
    for j in range(len(l)):
        if i!=j:
            if k[0]!=l[j][-1]:
                c+=1 
    if c==len(l)-1:
        string=k;l[i]='*' 
        break  
ans=[string]
while len(l)>0:
    h=[]
    for i in range(len(l)):
        if ans[-1][-1]==l[i][0]:
            ans.append(l[i]) 
            l[i]='*' 
            break  
    for i in l:
        if '*' not in i:
            h.append(i) 
    l=h  
print(ans)
