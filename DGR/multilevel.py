class calc1:
    def sum(self,a,b):
        return a+b
class calc2:
    def mul(self,a,b):
        return a*b
class calc3:
    def div(self,a,b):
        return a/b
class calc4:
    def sub(self,a,b):
        return a-b
ob1=calc4()
ob2=calc3()
ob3=calc2()
ob4=calc1()

print(ob4.sum(10,20))
print(ob3.mul(10,20))
print(ob2.div(20,10))
print(ob1.sub(20,10))       