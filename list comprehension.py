"""
You are given three integers X, Y, and Z representing the dimensions of a cuboid along
with an integer N. You have to print a list of all possible coordinates given by (i, j, k)
on a 3D grid where the sum of I + J + K is not equal to N.

Input FOrmat
Four integers X, Y, Z, and N each on four separate lines respectively.

Constraints
Print the list in lexicographic increasing order

"""

if __name__ == '__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    l = list()
    for i in range(x+1):
        for  j in range(y+1):
            for k in range(z+1):
                if(i + j + k != n):
                    l.append([i, j, k])
    print(l)
