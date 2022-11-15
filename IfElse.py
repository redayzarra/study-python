#Basics
temperature = 35 #Assigns the variable temperature to refer to value 30

if temperature > 30: #Creates a statement that executes if True
  print("It's a hot day!")
  print("Drink plenty of water!") #These statements will run because if is True
elif temperature > 20: #Runs if the above is False and this is True
  print("It's a nice day!")
elif temperature > 10: #Runs if none of the above conditions are True
  print("It's a cold day")
print("Done.") #Will always run because it is seperate from the if statement

#Practice
user_weight = float(input("Weight: ")) #Assigns the variable user_weight to the input from user, the input is converted to a float to except decimal values
units = input("(K)g or (L)bs: ") #Assigns the variable units to the input of the user

if units == "K" or "k": #Checks to see if the user input of units is the string K or k
  converted = user_weight * 2.2046 #If it is, then assign the variable converted to the product of the user_weight by 2.2046
  print("Weight in Lbs: " + str(converted)) #Print the string Weight in Lbs: followed by the string of the value of converted

elif units == "L" or "l": #If the statement above is not true, but if units is equal to L or l
  converted = user_weight * 0.4536 #Then assign the variable converted to the product of user_weight by 0.4536
  print("Weight in Kg: " + str(converted)) #Don't forget to convert to string!