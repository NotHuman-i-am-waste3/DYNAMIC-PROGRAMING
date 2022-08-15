s=input().strip()
l=list(map(str,input().split()))
i=0
def mal(s):
 s1=[]
 i=0
 while(i<len(s)):
    p=[1]
    for j in range(i+1,len(s)+1):
        if len(set(s[i:j]))==1:
            if len(s[i:j])>p[0]:
                p[0]=len(s[i:j])
    s1+=p
    i+=p[0]
 return s1
for i in l:
    print(mal(i),mal(s))