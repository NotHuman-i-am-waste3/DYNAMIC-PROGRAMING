n=int(input())
l=[input().strip() for i in range(n) ]
l1=[ i[0] for i in l ]
l2=[ i[-1] for i in l ]

ans=[ l[i] for i in range(n) if l1[i] not in l2  ]

while len(ans)!=n:
 for i in range(n):
    if ans[-1][-1]==l1[i]:
        ans.append(l[i])
print(ans)