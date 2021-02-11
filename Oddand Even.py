"""
Task
-------
Given an inter, n, perform the following conditional actions:
    -if n is odd, print Weird
    -if n is even and in the inclusive range of 2 to 5, print Not Weird
    -if n is even and in the inclusive range of 6 to 20, print Weird
    -if n is even and greater than 20 print Not Weird


"""
print("Please enter a number") #Asking user to input an integer

n = int(input()) #Converting input into integer

if (n % 2) != 0:  #-if n is odd, print Weird
    print("Weird")
    
elif (n % 2) == 0 and n in range(2,6):  #-if n is even and in the inclusive range of 2 to 5, print Not Weird
    print("Not Weird")
    
elif (n % 2) == 0 and n in range(6,21):   # -if n is even and in the inclusive range of 6 to 20, print Weird
    print("Weird")
    
else:   #-if n is even and greater than 20 print Not Weird
    print("Not Weird")


