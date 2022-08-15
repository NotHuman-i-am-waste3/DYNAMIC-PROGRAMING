l=[0,1,2]
c=0
for i in l:
   if i+2 or i-2 in l:
    print(i)
    c+=1
print(c/3)

