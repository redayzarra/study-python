#Basics
class Point: #Create a class object called Point
  def move(self): #Define different fucntions in this class
    print("move")

  def draw(self): #These functions often reference self
    print("draw")


point1 = Point() #Calls the class to any object
point1.x = 10 #Set different variables using the one calling the class
point1.y = 20 

print(point1.x) #Prints the value assigned to point1.x
point1.draw() #Call the draw function with the specified variable

point2 = Point() #Uses variable point2 to call the Point class
point2.x = 1 
print(point2.x)

#Constructors
class Point: #Create a class object called Point
  def __init__(self, x, y): #Constructor that gets called when new Point object is created, with the parameters x and y
    self.x = x #Self is a reference to the current object, the x attribute allows to reference the x parameter
    self.y = y

point = Point(10, 20) #Sets the value for x, y to 10 and 20 respectively
print(point.x) #Prints the value assigned to variable point.x

#Practice 
class Person: #Define the class as the word Person
  def __init__(self, name): #Define constructor function to add the parameter name
    self.name = name #Set the name attribute of the current object to the name argument passed through the method

  def talk(self): #Define the method talk and reference what this method does
    print("Talk") #The method talk just prints this string when initialized
    print(f"Hi, I am {self.name}") #Formatted string prints the string and the value that is passed for the name argument


ReDay = Person("ReDay Zarra") #Variable ReDay is calling the class with an argument for the parameter name
print(ReDay.name) #Print the name value associated with the name argument passed through
ReDay.talk() #ReDay is initializing the method talk to run the code above

De = Person(input("What is your name: ")) #Runs the user's input as the name argument
De.talk() #Calls the talk method with the current name argument