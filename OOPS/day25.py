
#SINGLE LEVEL
'''class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(self.emp_id, self.name)


class Child(Employee):
    def __init__(self, emp_id, name, time):
        super().__init__(name, emp_id)  # Call parent constructor
        self.time = time

    def version(self):
        print(self.emp_id, self.name, self.time)


# Object creation
obj = Child("EM102", "Arjun", "10:00 AM")
obj.version()

#MULTI LEVEL
class basicPlayer:
    def __init__(self,username):
        self.username=username
    def walk(self):
        print(self.username)
class warrior(basicPlayer):
    def attack(self):
        print(self.username)
class paladin(warrior):
    def heal(self):
        print(self.username)
hero=paladin("suresh")
hero.walk()
hero.attack()
hero.heal()


#MULTIPLE 
class imageContent:
    def apply(self):
        print("apply")
class text:
    def grammer(self):
        print("Scanning")
class Social(imageContent,text):
    def upload(self):
        print("postis now live")
my_post=Social()
my_post.grammer()
my_post.apply()
my_post.upload()'''
    
'''import  numpy as np
score=np.array([2,3,4,5,6])
mean=np.mean(score) 
median=np.median(score)
std_dev=np.std(score)
print(f"mean:{mean},median:{median},standard deviation:{std_dev}")'''

'''import numpy as np
arr=np.array([2,3,4,5])
print(arr[3])
print(arr[2])
arr2=np.array([[1,2,3],[2,3,4],[5,6,7]])
print(arr2[1,0])'''

s="programming"
result=""
for ch in s:
    if ch not in result:
        result=result+ch
print(result)

s=[1,2,2,3,4,4,5]
result=[]
for ch in s:
    if ch not in  result:
        result.append(ch)
print(result)