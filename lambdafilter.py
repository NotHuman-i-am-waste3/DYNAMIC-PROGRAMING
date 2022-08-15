# sorting only positive integers
l=[12,-5,7,-8,20,2,-1]
l=[58,2,-69,89,64,43,-29,-79,0,18,-30]
s=sorted([ i for i in l if i>=0])
ind=[i for i in range(len(l)) if l[i]>=0 ]
print(l)
j=0
for i in range(len(l)):
    if l[i]>=0:
        l[i]=s[j]
        j+=1
    if j>=len(ind):
        break
print(l)