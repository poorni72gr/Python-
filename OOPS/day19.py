class grandmother:
    name="poorni"
    def __init__(self,age):
        self.age=age
    def display(self):
        print(grandmother.name,self.age)
class mother(grandmother):
    name="preethu"
    def __init__(self,colour,age):
        grandmother.__init(self,age)
        self.colour=colour
    def show(self):
        print(mother.name,self.colour,grandmother.name,self.age)
class child(mother):
    name="bushan"
    def __init__(self,height,colour):
        mother.__init__(self,colour)
        self.height=height
    def version(self):
        print(child.name,self.height,mother.name,self.colour,grandmother.name,self.age)
obj=child(21,"pink",6)
obj.version()
