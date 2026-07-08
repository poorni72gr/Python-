'''class messenger:
    def use_keyboard(self):
        print("using tge keyboard")
    def send_message(self):
        print("this text message sent")
    def recieve_message(self):
        print("text message recieve")
class whatsapp(messenger):
    def send_message(self):
        print("text,video,audio sent using the wa")
    def recieve_message(self):
        print("text,video,audio recieve using the wa")
    def send_live_location(self):
        print("send the live location")
class facebookmessenger(messenger):
    def send_message(self):
        print("text,video,audio sent using the fb")
    def recieve_message(self):
        print("text,video,audio recieve using the fb")
    def use_built_apps(self):
        print("use the builtin apps")
class instamessenger(messenger):
    def send_message(self):
        print("text,video,audio sent using the im")
    def recieve_message(self):
        print("text,video,audio recieve using the im")
    def add_filters(self):
        print("add the filters")
def use_message(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.recieve_message()
    if type(ref)==whatsapp:
        ref.send_live_location()
    if type(ref)==facebookmessenger:
        ref.use_built_apps()
    if type(ref)==instamessenger:
        ref.add_filters()

wa=whatsapp()
fb=facebookmessenger()
im=instamessenger()

use_message(wa)
use_message(fb)
use_message(im)'''

'''print("secure connection has been established to the banks server")
try:
    p=int(input("enter  your principle amount:"))
    t=int(input("enter the duartion:10000"))
    r=10
    si=(p*t*r)/100
    print("simple intrest:",si)
except:
    print("please provde a numerical valus")
print("secure connection has been closed to the bank server:")'''

'''print("secure connection has been established to the banks server")
try:
    p=int(input("enter  your principle amount:"))
    t=int(input("enter the duartion:10000"))
    r=10
except: 
    print("please provde a numerical valus")
else:
     si=(p*t*r)/100
     print("simple intrest is:",si)
print("secure connection has been closed to the bank server:")'''

print("excecution started:")
lst=[12,20,0,30,40]
d={1:"c",2:"python",3:"java",4:"c++"}
try:
    r=int(input("enter the rank of the language:"))
    print(d[r])
    num=int(input("entre the index "))
    den=int(input("enter the index of denoinatoe:"))
    print(lst[num]/lst[den])
except KeyError e:
    print(e)
except 


   




       