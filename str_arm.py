s=S=input()

l=[ int(''.join(str(ord(i)))) for i in s]
#print(l)
suM=sum(l)
suMcheck=0
for i in l:
    suMcheck+=i**len(l)
nonduP=[]
if suMcheck==suM:

    for i in S:
        if i not in nonduP:
            nonduP.append(i)
    print(''.join(nonduP))
else:
    print(-1)

