n=int(input())
# l=list(map(int,input().split()))
# for i in range(n//2):
#     if l[i]%2==l[-i-1]%2:
#         a=l[-i-1]
#         l[-i-1]=l[i]
#         l[i]=a
# print(l)
l=[[1,2,3],[4,5,6],[7,8,9],[10,0,0]]
print(zip(*l))