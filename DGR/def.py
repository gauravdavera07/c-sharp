def bca():
    print("hello world")
bca()


def bca(sname):
    print(sname)
bca("Name")


def bca(sname):
    return(sname)
print(bca("Name"))
valueprint=bca("Name1")
print(valueprint)


def bca(sname="Dummy student"):
    return(sname)
print(bca())
print(bca("student"))

def bca(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
print(bca(1,2,3,4,5))

def bca(a,b):
    return(a+b)
i=int (input("enter no 1:"))
j=int (input("enter no 2:"))
sum=bca(i,j)
print(sum)    
    