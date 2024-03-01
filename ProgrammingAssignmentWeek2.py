

# Write a function to detect if given number m can be expressed as a sum of square of three numbers
# Return if m can be expressed as sum of three squares else false. 
# Assume m is a positive integer. If m is not positive return false
from asyncio.windows_events import NULL
import math
def threesquares(m):
    if m<=0 or math.modf(m)[0]>0 or math.modf(m)[1]<=0:
        return False
    # Legendre's theorem - If m can be written in the form 4^a(8b+7) then it can not be expressed as a sum of three squares
    while m%4==0:
        m=m/4
    if m%8==7:
        return False
    return True
print(threesquares(6))
print(threesquares(188))
print(threesquares(1000))
print(threesquares(7))
print(threesquares(15))
print(threesquares(71))
print(threesquares(1.2))
print(threesquares(-1))
print(threesquares(1.0))
print(threesquares(0.10))
print(threesquares(-1.1))
print(threesquares(-0.10))
for i in range(500):
    if not threesquares(i):
        print(i,end=', ')
# Write a function which detects if the given string s has any repeating chars. 
# Return true if no repetitions else return false.
def repfree(s):
    if s is not NULL and len(s)>0:
        print(set(s))
        print(len(set(s)))
        if(len(s)>len(set(s))):
            return False
    else:
        return False
    return True
repfree(NULL)
print(repfree('swatia'))
assert repfree("zb%78") == True , 'the string is repfree and should return True'
assert repfree("(7)(a") == False
assert repfree("a)*(?") == True
assert repfree("abracadabra") == False

#Version 2 of repfree
def repfree2(s):
    if s is NULL or len(s)<=0:
        return False
    x=[]
    for abra in s:
        if abra in x:
            print(x)
            return False
        x=x+[abra]
    print(x)
    return True
print(repfree2('asdfgah'))
print(repfree2('asdfgh'))
# Each sequence is at least of length 2. 
# Assume that consecutive numbers in the input sequence are different from each other.
# Input is 'l' which is a list of integers. 
# Returns true if l is a hill or a valley, and false otherwise.
def hillvalley (l):
    trend= []
    if len(l) in {0,1,2}:
        return False
    for a in range(1, len(l)):
        if l[a] >= l[a-1] and (len(trend)==0 or trend[-1]!='up'):
            trend.append('up')
        if l[a] <= l[a-1] and (len(trend)==0 or trend[-1]!='down'):
            trend.append('down')
    if len(trend) >2 or len(trend) ==1:
        return False
    if len(trend) ==2 and (trend[-1]=='up' or trend[-1]=='down'):
        return True
    return False
assert hillvalley([])==False
assert hillvalley([1]) == False
assert hillvalley([1,2]) == False
assert hillvalley([1,3,2]) == True
assert hillvalley([1,2,3,5,4]) == True

assert hillvalley([1,2,3,4,5]) == False

assert hillvalley([5,4,1,2,3]) == True

assert hillvalley([5,4,3,2,1]) == False
