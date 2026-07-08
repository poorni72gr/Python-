a= int(input("enter first angle:"))
b= int(input("enter second angle:"))
c= int(input("enter third angle:"))
if (a==b)and (b==c)and (c==a):
    print (" this is equilateral")
elif (a==b)or(b==c)or(c==a):
    print("this is isoscale")
else:
    print("this is scalar")
        
