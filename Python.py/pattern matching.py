'''n=3
for i in range(n):
    for j in range(n):
        print("*",end='')
    print()'''

'''n=5
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()'''
'''n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''

'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''

'''n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()'''
'''n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print("",end='')
    print()
n = 4

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

''''n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
        for k in range(1,2*i):
            if k == 1 or k == 2*i-1 or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
n = 6

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars and inner spaces
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''
'''n=5
num=1
for i in range(n):
    for j in range(i):
        print(num,end="")
        num=num+1
    print()

n=5
num=0
for i in range(n):
    for j in range(i):
        print(num ,end=' ')
    num= num+1
    print()'''

'''n=6
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=6
for i in range(n):
    for j in range(n):
        print(" ",end=" ")
        if i==0 or i==i+1 or j==0 or j==i+1:
            print("*",end=" ")
    print()'''

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()