class amazoncustomer:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def show(self):
        print("name:",self.name)
        print("email:",self.email)
class primeuser(amazoncustomer):
    def __init__(self,name,email,prime_id):
        self.name=name
        self.email=email
        self.prime_id=prime_id
    def show_prime(self):
        print("prime_id:",self.prime_id)
        print("benifits:free shipping")
class staffmember(amazoncustomer):
    def __init__(self,name,email,emp_id):
        self.name=name
        self.email=email
        self.emp_id=emp_id
    def show_staff(self):
        print("employee id:",self.emp_id)
        print("role:managerorders")
p1=primeuser("arjun","arjun23@gamil.com","WM124")
s1=staffmember("Meena","mee23@gmail.com","EM345")
p1.show()
p1.show_prime()
s1.show()
s1.show_staff()

class user:
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id
    def show_basic_details(self):
        print("name:",self.name)
        print("user id:",self.user_id)     
class seller(user):
    def __init__(self,name,user_id,product):
        user.__init__(self,name,user_id)
        self.product=product
    def show_product(self):
        print("Product:",self.product)
        print("Product delivery")
class delivery(user):
    def __init__(self,name,user_id,area):
        user.__init_(self,name,user_id)
        self.area=area
    def show_delivery(self):
        print("delibery area:",self.area)
class customer(user):
    def __init__(self,name,user_id,order):
        user.__init_(self,name,user_id,order)
        self.order=order
    def show_delivery(self):
        print("delibery area:",self.area)
class superadmin(customer,seller,delivery):
    def __init__(self,name,user_id,product,area):
        customer.__init__(self,name,user_id)
        seller.__init__(self,name,user_id,product)
        delivery.__init__(self,name,user_id,area)
def show_all_details(self):
    print("super admin")
    self.show_basic_details()
    self.show_customer_details()
    self.show_seller_details()
    self.show_delivey_details()
admin=superadmin(name="arjun",user_id=101,order=["laptop","mobile"],product=["shoes","watches"],area="bengaluru")
admin.show_all_details()



