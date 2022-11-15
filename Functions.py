#Basics
def greet_user(): #Creates a function with the name greet_user
  print("Hi there!")
  print("Welcome aboard!") #Print statements that run when function is called


print("Start")
greet_user() #Call the function, above code only gets executed when we call it
print("Finish!")

#Parameters
def greet_user2(name): #Creating a function that has the parameter name
  print(f"Hi there, {name}!") #Formatted print statement when function runs
  print("Welcome aboard!")

greet_user2("John") #Calling the function while providing arguments for name 
greet_user2("Mary") #The function must be provided with arguments to run

def greet_user3(first_name, last_name): #Functions can have multiple parameters
  print(f"Hi there, {first_name} {last_name}!") #Formatted string concatenation

greet_user3("ReDay", "Zarra") #Provide the function with necessary arguments


#Keyword Arguments
greet_user3(last_name = "Zarra", first_name = "ReDay") #Specifies which argument is what so order doesn't matter 

#Return Statement
def square(number): #Defines a function named square with parameter number
  return(number ** 2) #Returns the value of number squared

result = square(3) #Assigns variable return to the argument of 3 in the function
print(result) #Prints the variable result
print(square(3)) #Directly prints the result of the argument 3 from function


#Reusable Function
message = input("Type: ") #Assigns variable message to the user input

def emoji_converter(message): #Defines the function with parameter message
  words = message.split(" ") #Seperates message into individual words by spaces
  emojis = { #Creates a dictionary with keys and definitions
    "hello": "How you doin" 
  }
  output = "" #Create an empty output variable to store results in
  for word in words: #Iterate every word in the message one at a time
    output += emojis.get(word, word) + " " #Add the output to the word in the dictionary, if the word isn't there then keep the word, add a space, and then add that to output
  return(output) #Return the output value

print(emoji_converter(message)) #Print the result of the function with message


#Exceptions
