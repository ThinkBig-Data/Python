condition1 = True
x = 'python is easy' if condition1 else 'you need to work hard'
print(x)

#######################################

a=3
if a==0:
    print('zero true')
elif False:
    print('elif 1 true.')
elif False:
    print('elif 2 true.')
elif True:
    print('elif 3 true.')
elif False:
    print('elif 4 true.')
else:
    print('neither true')



######################################

m=42
k=72

if m<=k:
    print(f'{m}: is greater than {k}')
else:
    print(f'{m}: is lesser than {k}')


l = ('mukul', 'meenashki', 'reet', 'devansh', 'atul')
p = 'mukul'
for i in l:
    print(i)

if p == l[0]:
    print("codition true")
else:
    print('false')

###################################33

q = 5
w = 3

print(f'addition of {q} and {w} is {q+w}')
print(f'substraction of {q} and {w} is {q-w}')
print(f'multi of {q} and {w} is {q*w}')
print(f'division of {q} and {w} is {q/w}')
print(f'poewr of {q} and {w} is {q**w}')
