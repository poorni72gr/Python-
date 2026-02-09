'''for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()'''

#prime numbers

num=int(input("enter the value:"))
if num<=1:
    print("this is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("this is not aprime number")
            break
    else:
        print("this ia prime number")

    
 
'''num = int(input("Enter the value: "))

if num <= 1:
    print("This is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")'''
