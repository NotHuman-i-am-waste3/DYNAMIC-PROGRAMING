m=6
n=5
l=[list(map(int,input().split())) for _ in range(n)]

test = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

max_col = len(test[0])
max_row = len(test)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(test[y][x])
        rows[y].append(test[y][x])
        fdiag[x+y].append(test[y][x])
        bdiag[x-y-min_bdiag].append(test[y][x])

print(cols)
print(rows)
print(fdiag)
print(bdiag)
for i in (l):
    print(*i)