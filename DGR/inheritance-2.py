class animal():
    def sound(self):
        print("animal sound")
class dog(animal):
    def bark(self):
        print("dog is barking")
class babydog(dog):
    def eat(self):
         print("baby dog is eating")
d=babydog()
d.sound()
d.bark()
d.eat()