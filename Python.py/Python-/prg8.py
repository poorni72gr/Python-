'''num1=int(input("enter the number:"))
if num1%2==0:
    print("Odd number")
else:
    print("Even number")'''

'''num1=int(input("enter the number:"))
if num1<0:
    print("this is a negative")
elif num1>0:
    print("this is a posotive")
else:
    print("this is zero")'''


'''num=int(input("enter the number:"))
if num<=1:
    print("this is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("this is  not prime number")
            break
    else:
        print("this is a prime")'''
'''num = int(input("Enter the number: "))

if num <= 1:
    print("This is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")'''

'''start=int(input("enter the start number:"))
end=int(input("enter the end value:"))
print("the prime numbers in range :")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num %i==0:
                break
        else:
            print(num)'''


'''start=int(input("enter the value:"))
end=int(input("enter the value:"))
print("the prime numbers are range in:")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num7.Check if a number is in Fibonacci series7.Check if a number is in Fibonacci series)'''

'''num=int(input("enter the number:"))
fact=1
if num<=0:
    print("the prime number does not exit:")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial=",fact)'''

'''n=int(input("enter the number:"))
a=0
b=1
if n<=0:
    print("enter the positive number:")
elif n==1:
    print(a)
else:
    print("fibonaccci series:")
    print(a,b,end=" ")
    for i in range(2,n):
          c=a+b
          print(c,end=" ")
          a=b
          b=c'''
n=int(input("enter the number:"))
a,b=0,1
if n==0 or n==1:
    print("it is  a fibonacci series")
else:
    while b<n:
        a,b=b,a+b
    if b==n:
        print("it is a fibonacci")
    else:
        print("it is not a fibonacee")
    

    
