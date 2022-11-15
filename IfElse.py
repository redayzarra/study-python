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
user_weight = float(input("Weight: "))
units = input("(K)g or (L)bs: ")

if units == "K" or "k":
  converted = user_weight * 2.2046
  print("Weight in Lbs: " + str(converted))

elif units == "L" or "l":
  converted = user_weight * 0.4536
  print("Weight in Kg: " + str(converted)) #Don't forget to convert to string!