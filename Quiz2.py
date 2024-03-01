
#Quiz2:
print('#Quiz2:Question1')
x=[1,'abcd',2,'efgh',[3,4]]
y=x[0:6] # slicing/ substring is a new copy of the list
# and "out of bound" does not threw error in Python
print(x is y) #False
print(x==y)# True
z=x 
print(z is x)#True
print (z==x)#True
w=y
print(w is y)#True
print (w==y)#True
print(x[1][0:3]) # 'abc'
x[1]=x[1][0:3]+'d'
print(x) 
y[2]=4
print(y) #[1, 'abcd', 4, 'efgh', [3, 4]]
#z[1][1:3] = 'yzw' #TypeError: 'str' object does not support item assignment
#z[1][1:3] = z[1][1:3] + 'yzw' #TypeError: 'str' object does not support item assignment
# print('z before =')
#print(z)
#z[1]=z[1][1:3] + 'yzw' 
#print(z)
#k = z[1][1:3] + 'yzw'
#print(k)

#s='hello'
#s=s[0:3]+'p!'
#print(s)
z[0]=0
w[4][0]=1000
a=(x[4][1]==4)
print(a)
print(w)
#Quiz2:Answer1: # Statement 7
print("Quiz2:Answer1: # Statement 7")

print("Quiz2:Question2:")
x=[423,'b',37,'f']
u=x[1:]
y=u
w=x
u=u[0:]
u[1]=53
x[2]=47
print('x[2],y[1],w[2],u[1]')
print(x[2],y[1],w[2],u[1])
print("Quiz2:Answer2")

print("Quiz2:Question3:")
first = "tarantula"
second = ""
for i in range(len(first)-1,-1,-1):
  second = first[i] + second
  print(i)
print('second=')
print(second)
#class range(stop)
#class range(start, stop[, step])
# If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0.
# For a positive step, the contents of a range r are determined by the 
# formula r[i] = start + step*i where i >= 0 and r[i] < stop.
# For a negative step, the contents of the range are still determined by the 
# formula r[i] = start + step*i, but the constraints are i >= 0 and r[i] > stop.


print("Quiz2:Question4:")

def mystery(l):
    l[0]='swa' #notice that updating existing element caused change in list1
    print(l is list1) #True - update happened to same copy
    l=l+[90] # adding element to list1 created a new copy of list1, and did not add 90 to list1
    print(l is list1) #False -- copy is made 
    print(list1)
    print(l)
    l = l[0:5] # this statement also creates a new copy of list1 and leaves list1 alone
    print(l)
    print(list1)
    return()

list1 = [44,71,12,8,23,17,16]
mystery(list1)
print('list1')
print(list1)

###############################
import math
print(math.modf(1.234)[0])
print(math.modf(1.234)[1])