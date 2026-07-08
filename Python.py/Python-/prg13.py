'''n=input("entr the string:")
count=0
for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i:j+1]==n[i:j+1][::-i]:
            count += 1
print(count)'''


'''s=input("enter string:")
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            count += 1
print(count)'''


'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
while b!=0:
    a,b=b,a%b
print("the gcd:",a)'''

#square of number
'''n=5
for i in range(n):
    print("*" *n)'''


#right triangle
'''n=5
for i in range(1,n+1):
    print("*" *i)'''

#inverted triangle

'''n=5
for i in range(n,0,-1):
    print("*" *i)'''
#pyramid

 
'''n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)'''


stack=[]
stack.append(60)
stack.append(40)

stack.pop()
print(stack)



