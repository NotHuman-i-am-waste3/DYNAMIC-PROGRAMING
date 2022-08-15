import webbrowser


r,c=map(int,input().split())
l=[ list(map(int,input().split()))  for _ in range(r)]
c=[ [ j[i] for j in l ] for i in range(c)]
print(sorted(c,key=lambda x:sum(x)))

