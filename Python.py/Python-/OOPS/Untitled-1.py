class father:
    fathername="john"
    def __init__(self,age):
        self.age=age
    def show(self):
        print(father.fathername,self.age)
class mother:
    mothername="Arial"
    def __init__(self,height):
        self.height=height
    def display(self):
        print(mother.mothername,self.height)
class child(father,mother):
    childname="stenny"
    def __init__(self,colour,age,height):
        father.__init__(self,age)
        mother.__init__(self,height)
        self.colour=colour
    def version(self):
        print(father.fathername,mother.mothername,child.childname,self.age,self.height,self.colour)
obj=child(21,5,"pink")
obj.version()


s="aaabbbccdd"
result=""
count=1
for i in range(len(s)):
    if s[i]==s[i-1]:
        count=count+1
    else:
        result=result+s[i-1]+count
result=result+s[i]+1
print(result)


Class car:
    def __init__(self):
        self.color="pink"
        self.brand="Lamborgini"
        self.cost=1.2 crs
    def start_emgine(self):
        print("engine is starting")
c1=car()
print(c1.brand)
print(c1.colour)
print(c1.cost)
c1.start-engine()

a=[1,2,4]
total_sum=(n*(n+1)//2)
sum=0
for i in a:
    sum=sum+i
    missing=total_sum-sum
print(missing)