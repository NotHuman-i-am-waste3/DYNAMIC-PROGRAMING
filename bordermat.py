# see screenshot(304) for question
# r,s=map(int,input().split())
# c=r
# m=[list(map(str,input().split())) for i in range(r)]
# def vun(k):
#     l1=[m[k][i] for i in range(k,c-k)]
#     l2=[m[i][int(c-k-1)] for i in range(k+1,r-k)]
#     l3=[m[r-1-k][i] for i in range(k+1,c-1-k)][::-1]
#     l4=[m[i][k] for i in range(k+1,r-k)][::-1]
#     l=l1+l2+l3+l4
#     return l
# ans=[]
# for i in range(r):
#    ans += vun(i)
#    print(vun(i))
# print(ans)

mat=[[3],[2]]
li = []
while mat:
    li += mat.pop(0)
    print(li,mat)
    mat = (list(zip(*mat)))[::-1]
print(li)