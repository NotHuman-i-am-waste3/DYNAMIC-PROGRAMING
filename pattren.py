n=int(input())
m=[['-' for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            m[i][j]='*'
    print(*m[i])