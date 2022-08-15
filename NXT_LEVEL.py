'''
The program must accept an array of N integers as the input. The program must print the length of the longest arithmetic sequence in the given array as the output. An arithmetic sequence is a list of integers that contain at least two integers and the differences between consecutive integers are equal.

Boundary Condition(s):
1 <= T <= 100. T is the total number of test cases.
2 <= N <= 10^5
1 <= Each integer value <= 10^6

Input Format:
The first line contains T, followed by T test cases.
Each test case contains the input as below.
- The first line contains N.
- The second line contains N integers separated by a space.

Output Format:
For each test case, the first line contains Case #x: y, where x is the test case number (starting from 1) and y is the length of the longest arithmetic sequence in the given array.

Example Input/Output 1:
Input:
4
7
11 8 5 7 9 11 12
4
8 6 4 2
9
6 6 5 6 6 6 5 6 7
10
15 12 9 6 3 6 9 12 15 18

Output:
Case #1: 4
Case #2: 4
Case #3: 3
Case #4: 6

Explanation:
In test case 1: The longest arithmetic sequence is [5 7 9 11]. So its length 4 is printed.
In test case 2: The longest arithmetic sequence is [8 6 4 2]. So its length 4 is printed.
In test case 3: The longest arithmetic sequence is [6 6 6] or [5 6 7]. So its length 3 is printed.
In test case 4: The longest arithmetic sequence is [3 6 9 12 15 18]. So its length 6 is printed.

Example Input/Output 2:
Input:
6
10
10 10 7 7 9 1 1 1 1 1
10
8 8 7 5 1 5 7 10 1 8
15
1 9 18 26 3 10 10 8 6 9 4 8 5 10 3
10
5 5 4 3 10 4 2 2 3 8
14
4 4 2 6 8 10 12 2 1 4 1 3 1 4
15
10 6 2 1 1 1 3 2 5 6 5 4 3 2 1

Output:
Case #1: 5
Case #2: 2
Case #3: 3
Case #4: 3
Case #5: 4
Case #6: 6
'''
n=int(input())
for i in range(n):
    A=int(input())
    l=list(map(int,input().split()))
    c=[];ans=[];f=[]
    
    for a in range(len(l)-1):
        p=[l[a]-l[a+1]]
        q=[l[a]]
        for j in range(a+1,len(l)-1):
           if l[j]-l[j+1]==p[-1]:
            p.append(l[j]-l[j+1])
            q.append(l[j])
           else:
            break  
        c.append(q)
    print(c)
   
    # m=max([len(i) for i in c])
    # for i in range(len(c)):
    #     if len(c[i])==m:
    #         ans=c[i]+f[i]
    #         ans1=set(c[i])&set(f[i])

    # print(ans,ans1)
    # print(len(ans)-len(ans1))
