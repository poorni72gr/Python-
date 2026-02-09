'''a=[1,2,3,4,5,6]
start=0
end=len(a)-1
while start<end:
    a[start],a[end]=a[end],a[start]
    start=start+1
    end=end-1
print(a)'''

'''n=int(input("enter a number:"))
temp=n
revs=0
while temp>0:
    revs=revs*10+temp%n
    temp=temp//10
if revs==n:
    print("palandrome")
else:
    print("not pallindrome")'''

'''n=[1,2,3,454,565,667,67]
largest=0
for i in n:
    if i>largest:
        largest=i
print(largest)'''

'''n=[1,2,3,4,54,67]
largest=0
second_largest=0
for i in n:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=second_largest:
        second_largest=i
print(second_largest)'''

'''n=10
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,(a+b)'''

n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
    


