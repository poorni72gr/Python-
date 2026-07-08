'''num=int(input("enter the number:"))
temp=num
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10
if sum==num:
    print("Amstrong")
else:
    print("Not amstrong")'''



num=int(input("entr the number"))
temp=num
n=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp=temp//10
if sum==num:
    print("Amstrong")
else:
    print("Not amstrong")

    
