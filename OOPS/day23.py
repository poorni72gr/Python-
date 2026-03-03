s="abbbab"
largest=""
for i in range(len(s)):
    left,right=i,i
    while left>=0 and right<len(s) and s[left]==s[right]:
        if right-left+1>len(largest):
            latgest=s[left:right+1]
        left=left-1
        right=right+1
    left,right=i,i+1
    while left>=0 and right<len(s) and s[left]==s[right]:
        if right-left+1>len(largest):
            largest=s[left:right+1]
        left=left-1
        right=right+1
print(largest)

prices=[7,1,2,3,5,6]
profit=0
min=prices[0]
for price in prices:
    if price<min:
        min=price
    else:
        profit=max(profit,price-min)
print(profit)