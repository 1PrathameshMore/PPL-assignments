class Animals:
    
    def __init__(self):
        
        self.__eyes = 2     #Private variable __eyes
        self._living = True #Protected variable _living
        self.legs = 4       #Public variable legs
        
    def seteyes(self, eyes):
        self.__eyes = eyes
        
    def geteyes(self):
        return self.__eyes
    
    def getliving(self):
        return self._living
    
    def setliving(self, living):
        self._living = living
        
    def getlegs(self):
        return self.legs
    
    def setlegs(self, legs):
        self.legs = legs
        
    
class Lion(Animals):
    
    def eats(self):
        print("Lion eats meat!!")
        
    def color(self):
        print("Color of lion is Yellow!!")
        
    def sound(self):
        print("Lion Roar!!!!")
        
    def typeOfAnimal(self):
        print("Lion is a carnivoros animal!")
        

class Tiger(Animals):
    
    def eats(self):
        print("Tiger eats meat!!")
        
    def color(self):
        print("Color of tiger is Orange with black stripes")
        
    def sound(self):
        print("Tiger Roar!!")
        
    def typeOfAnimal(self):
        print("Tiger is a carnivoros animal!")
        

class Elephant(Animals):
    
    def eats(self):
        print("Elephant eats plant leaves!")
        
    def color(self):
        print("Color of elephant is Grey!!")
        
    def sound(self):
        print("Elephant Trumpet Sound!!!!")
        
    def typeOfAnimal(self):
        print("Elephant is a herbivoros animal!")
        
class Dog(Animals):
    
    def eats(self):
        print("Dog eats meat, veg food and dog food!")
        
    def color(self):
        print("Color of dog has a wide range!!")
        
    def sound(self):
        print("Bark!!!!")
        
    def typeOfAnimal(self):
        print("Dog is an omnivoros animal!!")
        
    
class Cat(Animals):
    
    def eats(self):
        print("Cats eat meat, veg food and cat food!!")
        
    def color(self):
        print("Color of cat has a wide range usually consisting of white,brown, black and red")
        
    def sound(self):
        print("Meow!!!!!")
        
    def typeOfAnimal(self):
        print("Cat is an omnivoros animal!")
        

class Monkey(Animals):
    
    def eats(self):
        print("Monkey eats vegetables and fruits!!")
        
    def color(self):
        print("Monkeys usually are brown!!")
        
    def sound(self):
        print("Monkey Sreeching Sound!!!")
        
    def typeOfAnimal(self):
        print("Monkey is an herbivoros animal!")
        
        
class Giraffe(Animals):
    
    def eats(self):
        print("Giraffe eats leaves!!")
        
    def color(self):
        print("Color of girrafe is brown or orange with white or cream colored stripes")
        
    def sound(self):
        print("Girrafe Flute like sound!!!")
        
    def typeOfAnimal(self):
        print("Giraffe is a herbivoros animal!")
        
    
class Zebra(Animals):
    
    def eats(self):
        print("Zebra eats leaves and branches of trees!!!!")
        
    def color(self):
        print("Color of zebra is white and black stripes!!")
        
    def sound(self):
        print("Zebra Bark!!! or Snort!!!")
        
    def typeOfAnimal(self):
        print("Zebra is a herbivoros animal!!")
        
    
class Kangaroo(Animals):
    
    def eats(self):
        print("Kangaroo eats vegetables, leaves!!!")
        
    def color(self):
        print("Color of Kangaroo is brown!!")
        
    def sound(self):
        print("Kangaroo Growls!!!! or Barks!!!")
        
    def typeOfAnimal(self):
        print("Kangaroo is a herbivoros animal!!")
        
    
class Dear(Animals):
    
    def eats(self):
        print("Dear eats leaves, vegetables!!!")

    def color(self):
        print("Color of dear is reddish or brown!")
        
    def sound(self):
        print("Dear Grunts!!! or Bleats!!!")
        
    def typeOfAnimal(self):
        print("Dear is a herbivoros animal!!!!")
        

leo = Lion()
#print(leo.__eyes)    This gives error as we cannot access private variables
print(leo._Animals__eyes) #This is one way to access private variables
print(leo._living)
print(leo.legs)
leo.eats()
leo.sound()
leo.color()
leo.typeOfAnimal()