n=int(input())
a=2*n-1
g=n
for i in range(n):
    o=n
    for j in range(i):
        print(o,end='')
        o=o-1
    for j in range(a-i*2):
        print(g,end='')
    p=g+1
    for j in range(i):
        print(p,end='')
        p+=1
    g=g-1
    print()






# o=[list(a*str(n))]
# b=n

# for i in range(1,n):
#     o1=o[-1][:i]+[ i for i in str(b-1)*(a-i*2)]+o[-1][:i][::-1]
#     o.append(o1)
#     b-=1
# for i in o+o[::-1][1:]:
#     print(''.join(i))