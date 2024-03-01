# This program prints Hello World
print("Hello World!!!!")
a, b = 0, 1
print(a,b)
while a<10:
    print(a)
    a,b=b,a+b

a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b

x=int(input('Please input and integer: '))

if x<0:
    x=0
    print('negative changed to 0')
elif x == 0:
    print('Zero')
elif x==1:
    print('single')
else:
    print('more')
