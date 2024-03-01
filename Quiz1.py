print("Assignment1:Q1")
def f(x):
    d=0
    while x > 1:
        (x,d) = (x/2,d+1)
    return(d)

def new_func(f):
    print("Ans1")
    print( f(27182818))
new_varnew_var = new_func(f)

print("Assignment1:Q2")
def h(n):
    s=0 # sum of factors of n
    for i in range(2,n):
        if(n%i==0):
            #s=s+1
            s=s+i
    return(s)
print(h(60))
print(h(45))
print("Ans2")
print(h(60)-h(45))

print("Assignment1:Q3")
def g(m,n):
    res=0
    while m>=n:
        (res,m)=(res+1,m/n)
    return(res)
print(g(375,4))

def FindDivisor(m,res):
    x=int(m**(1/res))
    return(x)
print("Ans3")
print(FindDivisor(375,4))

print("Assignment1:Q4")
print("Ans4")
print("The function terminates for positive n with mys(n) = factorial of n")
def mys(m):
    if m<=0:
       (m)=(-m)
    if m == 1:
        print( m,end='=')
        return(1)    
    else:
        print( m,end='*')
        return(m*mys(m-1))

print(mys(1),end='!')

