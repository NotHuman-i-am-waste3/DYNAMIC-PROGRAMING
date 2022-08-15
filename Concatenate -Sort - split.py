'''
The program must accept a list of integers and an integer K as the input. The program must form a new list of integers by concatenating every K integers in the given list. Then the program must sort those concatenated integers in ascending order. Finally, the program must split those concatenated integers to their original form and print them as the output.
Note: The number of integers in the given list is always divisible by K.

Boundary Condition(s):
0 <= Each integer value <= 10^4
1 <= K <= Number of integers in the given list

Input Format:
The first line contains a list of integers separated by a space.
The second line contains K.

Output Format:
The first line contains the integer value(s) separated by a space.

Example Input/Output 1:
Input:
4 56 0 789 12 3
2

Output:
12 3 4 56 0 789

Explanation:
Here K = 2.
After concatenating every two integers, the list contains 456, 0789 and 123.
After sorting those concatenated integers, the list becomes 123, 456 and 789.
Now, those integers are split to their original form as given below.
12 3 4 56 0 789

Example Input/Output 2:
Input:
98 467 1 5 7 67 0 18 0
3

Output:
0 18 0 5 7 67 98 467 1

Example Input/Output 3:
Input:
12 3 0 123 1 23
2

Output:
12 3 0 123 1 23
'''

l=['12','3','0','123','1','23']
k=2
ans=[]
for i in range(0,len(l),k):
    a=l[i:i+k]
    ans.append(a)
ans=sorted(ans,key=lambda x:int(''.join(x)))
print(ans)
