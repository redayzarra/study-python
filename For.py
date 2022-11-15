#Basics
numbers = [1, 2, 3, 4, 5]

for item in numbers: #Iterates over all the items in the list
  print(item)

i = 0
while i < len(numbers):
  print(numbers[i]) #Starts with i = 0 and then prints the element with that index
  i += 1

#Practice
prices = [10, 20, 30]

total = 0
for price in prices:
  total += price #Adds the value of price to total on every iteration
print(f"Total: {total}") #F-strings used to format string contacenation