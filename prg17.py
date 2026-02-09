'''n=[1,2,3,4,5,6]
start=0
end=len(n)-1
while start<end:
    n[start],n[end]=n[end],n[start]
    start=start+1
    end=end-1
print(n)'''
'''
n=int(input("enter the number:"))
temp=n
revs=0
while temp>0:
    revs=revs*10+temp%n
    temp=temp//10
if revs==n:
    print("palandrome")
else:
    print("not palindrome")'''


'''n=[1,2,3,4,5,65,67]
largest=0
for i in n:
    if i>largest:
        largest=i
print(largest)'''


'''n=[1,2,3,4,565,43,321]
largest=0
s_l=0
for i in n:
    if i>largest:
        s_l=largest
        largest=i
    elif i>s_l and i!=s_l:
        s_l=i
print(s_l)'''


'''n=10
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,(a+b)'''

n=int(input("ener the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

