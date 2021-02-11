"""
Task
-----

Read an integer N. For all non-negative integers i<N, PRINT i to the power of 2.
See the sample for details.

Input Formats
-----------

The first and only line contains the integer, N.

Constraints
1<=N<=20

Output Format
Print N lines, one corresponding to each i.



"""

print("Please enter a number")
n = int(input())
for i in range(0,n):
    print(i*i)
