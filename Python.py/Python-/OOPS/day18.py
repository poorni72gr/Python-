class Parent:
    legs = 4

    def __init__(self, legs):
        self.legs = legs
        print("This is parent constructor")

    def show(self):
        print("This is parent method")


class Father(Parent):
    def __init__(self, colour, **kwargs):
        self.colour = colour
        super().__init__(**kwargs)
        print("This is father constructor")

    def show(self):
        print("This is father method")


class Mother(Parent):
    def __init__(self, height, **kwargs):
        self.height = height
        super().__init__(**kwargs)
        print("This is mother constructor")

    def show(self):
        print("This is mother method")


class Child(Father, Mother):
    def __init__(self, name, colour, height):
        self.name = name
        super().__init__(colour=colour, height=height, legs=2)
        print("This is child constructor")

    def show(self):
        print("This is child method")
        print(self.name, self.colour, self.height, self.legs)


obj = Child("Ravi", "White", 5.6)
obj.show()


s="python!@#$%gto5&*"
result=""
for ch in s:
    if ch.isalnum():
        result=result+ch
print(result)

s = "Hello@123#World!"
special = ""

for ch in s:
    if not ch.isalpha() and not ch.isdigit():
        special += ch

print(special)
height=[4,2,0,4,1,5]
left=0
right=(len(height)-1)
left_max=0
right_max=0
result=0
while left<right:
    if height[left]<height[right]:
        if height[left]>=left_max:
            left_max=height[left]
        else:
            result=result*left_max-height[left]
            left=left+1
    else:
        if height[right]>=right_max:
            right_max=height[right]
        else:
            result=result+right_max-height[right]
            right=right-1
print(result)


a = [1, 2, 4]

n = 4   # highest number in the range
total_sum = n * (n + 1) // 2

current_sum = 0
for i in a:
    current_sum = current_sum + i

missing = total_sum - current_sum
print(missing)
height=[4,2,0,4,1,5]
left=0
right=(len(height)-1)
left_max=0
right_max=0
result=0
while left<right:
    if height[left]<height[right]:
        if height[left]>=left_max:
            left_max=height[left]
        else:
            result=result*left_max-height[left]
            left=left+1
    else:
        if height[right]>=right_max:
            right_max=height[right]
        else:
            result=result+right_max-height[right]
            right=right-1
print(result)
            


     
