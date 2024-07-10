class base:
  def _init_(self):
     self.name=77
class dervied(base):
    def _init_(self):
     print ("we will call the protected members of base class"(self.name))
     self.name=150
     print("we will call the modified protected members outs ")
obj1=dervied()
obj2=base()  
print("access objects 1", obj1.name) 
print ("acsess objects 2",obj2.name)  