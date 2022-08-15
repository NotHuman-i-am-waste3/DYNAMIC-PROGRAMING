
def ca():
        l=[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
        m=n=len(l)-2
        le=len(l)
        ans=[]
        for k in range(m):
         mat=[]
         i=0
         while(i<len(l)-2):
            s=[]
            for p in range(i,i+3):
                a=l[p][k:k+3]
                s+=a
            i+=1
            mat.append(max(s))
         ans.append(mat)
        # print(ans)
        ans1=[]
        for i in range(m):
            p=[ j[i] for j in ans ]
            ans1.append(p)
        return ans1

print(ca)