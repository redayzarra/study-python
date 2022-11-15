#Basics
for x in range(4): #Creating a range from 0 to 4 while excluding 4
  for y in range(3): #Creating a range from 0 to 3 while excluding 3
    print(f"({x}, {y})") #Will continue until inner loop completes

#Practice
numbers = [1, 1, 1, 1, 4] #Create an array called numbers

for x_count in numbers: #Iterate through every element of numbers and assign that value to x_count
  output = '' #Create a variable called output that refers to an empty string
  for count in range(x_count): #Iterate through the loop however much the value of an element in numbers is, assign that element value as count
    output += "x" #Add the string x to variable output every loop
  print(output) #Print the string assigned to output after the initial for loop is completed