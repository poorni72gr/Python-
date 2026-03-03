n=[2,4,5,6,7,8]
largest=0
second_largest=0
while i>largest:
    second_largest=largest
    largest=i
if i>second_largest and i!=second_largest:
    second_largest=i
print(second_largest)
#keyword arguments
def login(users,password):
    print(users,password)
login(password="1234",users="admin")

#varivale length arguments
def total(*nums):
    print(sum(nums))
total(10,20,30)

