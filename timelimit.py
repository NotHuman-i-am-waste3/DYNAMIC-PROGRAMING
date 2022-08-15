n=int(input())
k=int(input())
a=''.join(sorted(str(n))[::-1])
c=1
for i in range(1,int(a)+1):
    if (''.join(sorted(str(i))) in str(n)) or (''.join(sorted(str(i))) in ''.join(sorted(str(n)))) or ''.join(sorted(str(i))[::-1]) in str(n):
        if c==k:
            print(i)
            exit()
        c+=1

print(-1)
