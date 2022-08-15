s=input()
S=list(s)

for i in range(1,len(s)-1):
    if s[i] in 'aeiouAEIOU':
        if ord(s[i-1])>=65 and ord(s[i-1])<97:
            S[i-1]=chr(ord(s[i-1])+32)
        else:
            S[i-1]=chr(ord(s[i-1])-32)

        if ord(s[i+1])>=65 and ord(s[i+1])<97:
            S[i+1]=chr(ord(s[i+1])+32)
        else:
            S[i+1]=chr(ord(s[i+1])-32)
print(''.join(S))
# print(chr(ord('a')-32))
