#Basics
numbers = range(5)
print(numbers) #Returns the range of numbers from 0 to 5 but excluding 5

for number in numbers:
  print(number) #Prints the numbers in the range, except for 5

numbers = range(5, 10) #Creates a range from 5 to 10 but excluding 10
for number in numbers:
  print(number)

numbers = range(5, 10, 2) #Creates a range from 5 to 10, in increments of 2
for number in numbers:
  print(number)

for number in range(5): #Automatically finds the numbers within the range
  print(number)