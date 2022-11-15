#Basics
numbers = [1, 2, 3, 4, 5] #Creates an array called numbers

for item in numbers: #Iterates over all the items in the list
  print(item)

i = 0
while i < len(numbers): #Executes the code below if the value for i is less than the length of array numbers
  print(numbers[i]) #Starts with i = 0 and then prints the element with that index
  i += 1 #If the statement above is met, then increase the value of i by one every time

#Practice
prices = [10, 20, 30] #Create an array called prices

total = 0 #Assign the value of total to zero
for price in prices: #Iterate through every element in prices and assign the value to price every loop
  total += price #Adds the value of price to total on every iteration
print(f"Total: {total}") #F-strings used to format string contacenation