#Basics
class Dog: #Creates a class object called Dog
  def walk(self): #Creates a method called walk that references self
    print("walk") #Method executes this print statement when it's initialized


class Cat: #Another class object Cat wants to use the same walk method
  def walk(self): #It is bad practice to reuse code
    print("walk")

#Inheritance
class Mammal: #Creates a class object called Mammal 
  def walk(self): #Creates a method called walk that references self
    print("walk") #This string is printed when the method walk is initialized


class Dog(Mammal): #Class object Dog is able to inherit all methods from Mammal
  def bark(self): #Creating a method called bark that executes following code
    print("Bark") #String is printed if walk method is initialized


class Cat(Mammal): #Class Cat is inheriting all methods from class Mammal
  def meow(self):
    print("Meow")


class Horse(Mammal):
  pass #Means nothing, allows Python to skip this line without errors

dog1 = Dog() #Variable dog1 is calling the Dog class object
dog1.walk() #Variable is initializing the walk method inherited from Mammal
dog1.bark()

cat1 = Cat()
cat1.meow()