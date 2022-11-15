#Basics
print("Hello World") #This statement prints whatever is in the quotes to the console
print('Hello World') #Double quotes and single quotes return the same result
print(3) #This statement will print whatever value is in the parenthesis

a = 1 #Assigns the variable a to value of 1
print(a) #Prints whatever value is assigned to a

b = 2 #Different variables can be assigned to values
print(b)

c = 'hello there' #The varible c is assigned to the string hello there
print(c)

d = 2 #Two variables can refer to the same value
b = 1 #The variable b is now referring to 1 because it is the latest command
b = "ahhh" #The variable b is now a string called ahhh
print(b) #Returns ahhh because that is the latest value assigned to b

f = a #The variable f now refers to the same value as variable a 

#Practice Problem: Swap the two variables 
v1 = 'first string'
v2 = 'second string'

#Solution 1 - Create two temporary variables
temp1 = v1
temp2 = v2 #Creating temporary variables for the originals to refer to

v1 = temp2
v2 = temp1 #Assign the values to the temporary variables

#Solution 2 - Create one temporary variable 
temp = v1 #Create the temporary variable referring to v1

v1 = v2 #Assign v1 to the value of v2
v2 = temp #Assign v2 to the value of temp1 which was referring to v1

#Basics
age = 20
price  = 19.95
first_name = "ReDay" #Good practice to seperate words with underscores
is_online = False #The word False has to be capitalized

print(age) #Prints the value that is assigned to a 

#Practice 
age = 20
status = "new patient"
name = "John Smith"
