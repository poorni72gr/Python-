'''class customer:
    def __init__(self,name,ph,email):
        self.name=name
        self.ph=ph
        self.email=email
class platinumcustomer(customer):
    def __init__(self,name,ph,email,plat_id):
        self.name=name
        self.ph=ph
        self.email=email
        self.plat_id=plat_id
    def display(self):
        print(self.__dict__)
p=platinumcustomer("arjun",22334455677,"arjun23@gmail.com",10)
p.display()'''

class messenger:
    def send_message(self):
        print("text message is sent")
    def recive_message(self):
        print("text message is recive")
class internalmessenger(messenger):
    pass
class whatsappmessenger:
    def send_message(self):
        print("text,potos,vidous&filters is sent")
    def recive_message(self):
        print("tect,photos,videos&files recived")
    def set_dp(self):
        print("dp is set")
    def set_status(self):
        print("status is sent")
im=internalmessenger()
im.send_message()
im.recive_message()
wam=whatsappmessenger()
wam.send_message()
wam.recive_message()
wam.set_dp()
wam.set_status()

