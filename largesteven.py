n=input()
s=''
for i in n:
    if i not in s and i.isdigit():
        s+=i
s1=sorted(s)
S=sorted(s)[::-1]
c=0
for i in S:
    if int(i)%2==0:
        c=1
if (c==0):
    print(-1)
    exit()
for i in range(len(S)-1,0,-1):
    if int(S[i])%2==0:
        p=S.pop(i)
        S+=p
        break
print(S)

