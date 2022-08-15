
n=int(input())
l=[['#' for i in range(n*2)] for j in range(n)]
l[0][n-1]='/'
l[0][n]=r'\ '[0]
print(''.join(l[0]))
a=n-2
b=n+1
p=1
for i in l[1:]:
   if p%2==0:
    i[n-1]='/'
    i[n]=r'\ '[0]
   i[a]='/'
   i[b]=r'\ '[0]
   for j in range(a+1,n-1):
    if j%2==a%2:
        i[j]='/'
   for j in range(n+1,b):
    if j%2==b%2:
        i[j]=r'\ '[0]
   a-=1;b+=1;p+=1
   print(''.join(i))
L=l[::-1]
for i in L:
    s1=''.join(i[:n]).replace('/',r'\ '[0])
    s2=''.join(i[n:]).replace(r'\ '[0],'/')
    # s=s.replace(r'\ '[0],'/')
    print(s1+s2)
    
