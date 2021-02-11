"""
Arithmetic Operators
-------------------

Task
---
Read two integers from STDIN and print three lines where;
    -The first line contains the sum of the two numbers.
    -The second line contains the difference of the two numbers(first-second)
    -The third line contains the product of two numbers

Input Formats
------------
The first line contains the first integer, a. The sedont line contains second
integer, b.

Constraints
-----------
1<=a<=10 to the power of 10
1<=b<=10 to the power of 10

Output format
------------
Print the three lines as explained above 

"""
print("Print the first number")
a = int(input())
print("Print the second number")
b = int(input())

print(a + b)
print(a - b)
print(a * b)
