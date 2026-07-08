'''lst=[1,2,3,4,5]
print(lst)'''

'''lst=[1,2,3,4,5]
lst.append([6])
print(lst)'''


'''lst=[1,2,3,4,5]
lst.extend([6,5,6,7])
print(lst)'''

'''lst=[1,2,3,4,5]
lst.insert(2,8)
print(lst)'''

'''lst=[1,2,3,4,5]
lst.pop(3)
print(lst)'''

'''lst=[1,2,3,4,5]
lst.remove(4)
print(lst)'''

'''lst=[1,2,3,2,1,2,2,3,4,5]
print(lst.count(2))'''

'''lst=[1,2,3,4,5]
print(len(lst))'''

'''lst=[1,2,3,4,5]
print(lst[1:2])'''

#sum of number without using the built in function
'''lst=[1,2,3,5]
sum=0
for i in lst:
    sum=sum+i
print(sum)'''

'''lst=[1,2,3,5]
sum=0
for i in lst:
    sum=sum+1
print(sum)'''

#To find the missing value

a=[1,2,4,5,6]
n=6
sum=0
total=(n*(n+1))//2
for i in a:
    sum=sum+i
missing=total-sum
print(missing)

# to remove the duplicate values
'''a=[1,2,1,2,3,4,2,1]
emp=[]
for i in a:
    if i not in emp:
        emp.append(i)
print(emp)'''


#break statement
'''a=[1,2,3,4,5]
for i in range(1,5):
    if i==5:
        break
print(i)'''


# continue statement
'''a=[1,2,3,4,5,6]
for i in range(1,6):
    if i==6:
        continue
    print(i)'''



        
