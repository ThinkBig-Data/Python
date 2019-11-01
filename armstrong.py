x=int(input('enter any three digit number to find whether it is an armstrong number or not'))
a=x%100
a=a%10
b=x%100
b=b//10
c=x//100
n=(a**3)+(b**3)+(c**3)
if n==x:
    print(x," is an armstrong number")
else:
    print(x,' is not an armstrong number')
