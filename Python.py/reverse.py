'''n=234
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print(rev)

n=131
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if n==rev:
    print("palindrom")
else:
    print("not palindrome")

n=232
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")

n=5
a=1
b=0
for i in range(n):
    print(a)
    a,b=b,a+b'''

'''n=int(input("enter the number"))
count=0
if n==0:
    count=1
else:
    while n!=0:
        count=count+1
        n=n//10
print(count)'''

'''a=int(input("enter the number"))
b=int(input("enter the number"))
while b!=0:
    a,b=b,a%b
print("the gcd of to number is",a)'''

'''a=int(input("enter the number"))
b=int(input("enter the number"))
x=a
y=b
while y!=0:
    x,y=y,x%y
lcm=(a*b)//x
print("the lcm of two numbers is:",lcm)'''

'''n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")'''

'''str="madam"
if str==str[::-1]:
    print('palindrom')
else:
    print('not a palindrom')'''

'''str="programming"
unique=""
for ch in str:
    if ch not in unique:
        unique =unique+ch
print(unique)'''

'''str="python proramming lan"
word=""
max_word=""
for ch in str:
    if ch!="":
        word=word+ch
    else:
        if len(word)>=len(max_word):
            max_word=word
        word=""
if len(word)>len(max_word):
    max_word=word
print("the largest word is :",max_word)'''

'''arr=[1,2,3,2,3,1]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)'''

'''n=[2,3,4,5,6]
max=n[0]
for i in n:
    if i>max:
        max=i
print(max)

n=[2,3,4,5,6]
min=n[0]
for i in n:
    if i<min:
        min=i
print(min)'''

'''n=[2,5,6,7,4,3]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
print(n)'''

'''a=[1,2,3,4]
b=[2,31,4]
for i  in a:
    if i in b:
        print(i)

a=[1,2,3,4]
b=[1,2,3,4]
c=a+b
print(c)

n=[1,2,3,4,5,6,7,8,9]
even=0
odd=0
for i in n:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)

n=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)'''

'''n=[1,2,3,4]
sum=0
for i in range(len(n)):
    sum=sum+n[i]
print(sum)

n=[1,2,3,4]
sum=0
for i in range(len(n)):
    sum=sum+n[i]
average=sum/len(n)
print(average)

arr=[1,2,3,4,5]
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start=start+1
    end=end-1
print(arr)

n=[1,2,3,4,5]
smallest=n[0]
for i in n:
    if i<smallest:
        smallest=i
print(smallest)

str="programming"
for i in range(len(str)):
    count=0
    for j in range(len(str)):
        if str[i]==str[j]:
            count=count+1
    if count==1:
        print("the sum is:",str[i])
        break'''

'''str="programming"
for i in range(len(str)):
    count=0
    for j in range(len(str)):
        if str[i]==str[j]:
            count=count+1
    if count==1:
        print(str[i])

str="programming"
for i in range(len(str)):
    count=0
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            count=count+1
            break
        else:
            continue
            break

str="madam"
result={}
for i in str:
    if i in result:
        result[i]=result[i]+1
    else:
        result[i]=1
print(result)'''

str="madam"
result=""
for ch in str:
    if ch not in result:
        result=result+ch
print(result)

str="python programming lang"
word=""
max_word=""
for ch in str:
    if ch!=" ":
        word=word+ch
    else:
        if len(word)>len(max_word):
            max_word=word
            word=""
if len(word)>len(max_word):
    max_word=word
print(max_word)


