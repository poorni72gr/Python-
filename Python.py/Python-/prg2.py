'''num1=int(input("poorenter num1:"))
num2=int(input("enter num2:"))
print(num1-num2)'''

'''s1=int(input("enter the himalayan speed:"))
s2=int(input("enter the mud road speed:"))
s3=int(input("enter the highway speed:"))
avg=(s1+s2+s3)/3
print(avg)'''
       

'''rama_height=1.3
raja_height=1.7
if rama_height!=raja_height:
    print("rama is taller")
else:
    print("raja is taller")'''

'''user_name=input("enter the user name:")
password=input("enter the user pssword:")
if user_name=="john" or password=="":
    print("login successfully")
else:
    print("login failed")'''

'''r1=int(input("enter the poorni rank:"))
r2=int(input("enter the bushan rank:"))
r3=int(input("enter the preethu rank:"))
r4=int(input("enter the reddy rank:"))
if r1>r2 and r1>=r3 or r1>r4:
    print("poorni as the highest:",r1)
elif (r2<21) and (r2<r3) or (r2<r4):
    print("bushan as the highest:",r2)
elif (r3>r1) and (r3>r2) and (r3>r4):
    print("preethu as the highest:",r3)
else:
    print("reddy as the highest:",r4)'''
 
'''s1=int(input("enter the student1 :"))
s2=int(input("enter the student2 :"))
s3=int(input("enter the student3 :"))
s4=int(input("enter the student4 :"))
marks=[("student",s1),("student2",s2),("student3",s3),("student4",s4)]
marks.sort(key=lambda x: x[1],reverse=True)
print("first rank",marks[0][0],"-",marks[0][1])
print("second rank",marks[1][0],"-",marks[1][1])
print("third rank",marks[2][0],"-",marks[2][1])
print("forth rank",marks[3][0],"-",marks[3][1])'''

r1 = int(input("Enter marks of reddy 1: "))
r2 = int(input("Enter marks of preethu 2: "))
r3 = int(input("Enter marks of bhushan 3: "))
r4 = int(input("Enter marks of poorni 4: "))
marks = [r1, r2, r3, r4]
marks.sort(reverse=True)   
print("Rank  1:", marks[0])
print("Rank 2:", marks[1])
print("Rank 3:", marks[2])
print("Rank 4:", marks[3])







    



