'''lst=[1,2,3,5]
emp_lst=[]
for x in lst:
    if x%2==1:
        emp_lst.append(x)
print(emp_lst)'''

#list comprehension
'''lst=[1,2,3,5]
print(["odd" if x%2==1 else "even" for x in lst ])'''


'''lst=[[1,2,3,5],[7,9,11]]
print([y for x in lst for y in x if y%2==1])'''

'''lst=[[1,2,3,5],[7,9,11]]
for x in lst:
    print(sum(x))'''

for x in [[1,2,3,5],[7,8,9,4]]:
    sum=0
    for y in x:
        sum=sum+y
    print(sum)
