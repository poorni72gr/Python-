class accountHolder:
    def __init__(self):
        self.bal=10000
    def get_bal(self):
        return self._bal
    def set_bal(self,amt):
        if amt>0:
            self._bal=amt
        else:
            print('invalid amiunt')
ah=accountHolder()
print(ah.bal)
ah.bal=-20000
print(ah.bal)

class accountHolder:
    def __init__(self):
        self._bal=10000
    def get_bal(self):
        return self._bal
    def set_bal(self,amt):
        if amt>0:
            self._bal=amt
        else:
            print('invalid amiunt')
ah=accountHolder()
print(ah.get_bal())
ah.set_bal(-20000)
print(ah.get_bal())

class accountHolder:
    def __init__(self):
        self.__bal=10000
    def get_bal(self):
        return self.__bal
    def set_bal(self,amt):
        if amt>0:
            self.__bal=amt
        else:
            print('invalid amiunt')
ah=accountHolder()
print(ah.__dict__)
print(ah._accountHolder__bal)
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
#METHOD DECORATOR
#IT USED INSIDE THE CLASS NOT AN OBJECT IT USED  TO HANDLE THE SELF KEYWORD FOR INSTANCE METHOD
def dec(fun):
    def wra(self,name):
        print("going")
        print("coming")
        fun(self,name)
    return wra
class student:
    @dec
    def f1(self,name):
        print("work1",name)
    def f2(self,name):
        print("work2",name)
obj=student()
obj.f1('poorni')
obj.f2('naga')
#CLASS DECORATOR
#IT IS USED TO MODIFY AND ENHNACE THE BEHAVIOR OF THE CLASS
def dec(cls):
    def greet(self):
        print("hello student")
    cls.greet=greet
    return cls
@dec
class student:
    pass
s=student()
s.greet()

#CALENDER
import calendar
year=2026
month=3
cal=calendar.month(year,month)
print(cal)

