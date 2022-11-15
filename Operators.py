#Basics
print(10 + 3) #Adds 10 and 3 
print(10 - 3) #Subtracts 10 and 3
print(10 * 3) #Multiplies 10 and 3 
print(10 / 3) #Divides 10 with 3 and returns a float (number with decimals)

#Types of Division
print(10 // 3) #Divides 10 with 3 but returns only the whole number
print(10 % 3) #Divides 10 with 3 and only returns the remainder 

print(10 ** 3) #Puts 10 to the power of 3 

x = 10 #Assigns variable x to the value of 10
x = x + 3 #Assigns variable x to the sum of the last value of x and 3 
x += 3 #This is exactly the same as the command above: x = x + 3

x *= 3 #This translates to x = x * 3

#Operator Precedence
x = 10 + 3 * 2 #Multiplication has higher priority so 6 is added to 10
x = (10 + 3) * 2 #Use parenthesis to do specify those calculations first

#Comparison Operators
x = 3 > 2 #Boolean expression because it returns the value True 
x = 3 >= 3 #Returns True because 3 is greater than or equal to 3
x = 3 == 3 #Returns True because 3 is equal to 3
x = 3 != 2 #Returns True because 3 is not equal to 3

#Logical Operators
price = 25
print(price > 10 and price < 30) #Returns True because it is True AND True
print(price > 10 or price < 30) #Returns True because it is True or True
price = 5
print(price > 10 or price < 30) #Returns True because it is False or True
print(not price > 10) #Returns True because it is NOT False