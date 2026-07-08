'''units=int(input("enter electricity units:"))
if units<=100:
    bill=units*1
elif units<=200:
    bill=100*1+(units-100)*2
else:
    bill=100*1+100*2+(units-200)*5
print("Electricity bill:",bill)'''

pin=int(input("enter the pin:"))
balance=5000
if pin==1234:
    amount=int(input("enter withdrawal amount:"))
    if amount<=balance:
        print("Withdrawal successfukl.")
    else:
        print("insufficient balance")
else:
    print("wrong pin")
