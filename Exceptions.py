#Basics
age = int(input("Age: ")) #Assign the variable age to the integer value of the user's input
print(age) #Print the value for age

try: #Try running the following code, if it works then execute it
  age = int(input("Age again:")) #Assigns the value of age to the integer value of the input
  print(age) #Print the value of age, if age is an integer

except ValueError: #If the users input is not the right value, they didn't write numbers that can be converted to strings, then execute the following code
  print("Invalid value") #Print this string if the try block code does not work


try: #Try the following code, if it doesn't work then follow the exceptions below
  age = int(input("Age: ")) #Assign variable age to the integer value of user's input
  income = 20000 #Assign variable income to 20000
  risk = income / age #Assign the variable risk to the dividend of income and age
  print(risk) #Print the value of risk

except ValueError: #If the user's input value is incorrect, like a string that can't be converted into a integer, then run the following exception code
  print("Invalid value") #Print this string back to the console for a ValueError

except ZeroDivisionError: #If the user's input cannot be used for calculations, like an input of zero for division, then run the folloiwng exception code
  print("Age cannot be zero!") #Print this string back to console 