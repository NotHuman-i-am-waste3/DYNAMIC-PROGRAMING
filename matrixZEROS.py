
''' if any zero is present in the matrix convert that corresponding column and row elemts to zero
here i hae taking index of tht 0 and checking tht row and coumn index if equal converting to zero
for eg:
the given mtrix is:
1 1 0 1 
0 1 1 1
1 0 1 1 
1 1 1 1 
the output will be:
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 1'''

# 1st method:

n=int(input())
m=int(input())
l=[ list(map(int,input().split()))  for _ in range(n)]
ind=[];rind=[]
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            ind.append(i)
            rind.append(j)
for i in range(n):
    for j in range(m):
        if i in ind:
            l[i][j]=0
        if j in rind:
            l[i][j]=0
for i in l:
    print(*i)
# 2 nd method
# n=int(input())
# m=int(input())
# l=[ list(map(int,input().split())) for _ in range(n)]
# row=[]
# col=[]
# for i in range(n):
#     for j in range(m):
#         if l[i][j]==0:
#             col.append(j)
#             row.append(i)
# for i in row:
#     l[i]=[0]*m
# for i in range(m):
#     for j in l:
#          if i in col:
#             j[i]=0
    
# for i in l:
#     print(*i)