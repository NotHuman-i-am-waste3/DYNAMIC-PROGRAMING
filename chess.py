n=int(input())
l=[input().strip() for _ in range(n)]
C=[]
for i in range(n):
    k=''.join([ j[i] for j in l ])
    C.append(k)

if n%2==0 : 
 a=n//2*'WB';b=n//2*'BW';c=a;d=b
else: a=n//2*'WB';b=n//2*'BW';c=a+'W';d=b+'B'
def check(l,a,b,c,d,n):
 ans=[ i for i in l if i==a or i==b or i==c or i==d]
 if len(ans)==n: 
    print("Valid")
 else: 
    print("Invalid")
print(check(l,a,b,c,d,n))
print(check(C,a,b,c,d,n))
