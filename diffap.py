l=[5,1,3,4,2]
c=0
# [5,3] ,[4,2] ,[3,1]
'''s=set(l)
c=0
for i in range(len(l)):
    s=[l[i]-j for j in l[i+1:]]
    # if len(s)!=0:
    #  c+=1
    print(s)'''
diff=2 
for i in l:
    if i+diff in l:
        c+=1
print(c)


# for a in range(len(l)-1):
#         p=[l[a]-l[a+1]]
#         q=[l[a]]
#         for j in range(a+1,len(l)-1):
#            if l[j]-l[j+1]==p[-1]:
#             p.append(l[j]-l[j+1])
#             q.append(l[j])
#            else:
#             break  
#         c.append(q)
# print(c[0])