#Basics
numbers = (1, 2, 3, 3) #Creates a tuple that cannot be edited
numbers.count(3) #Counts the number of times the number 3 shows up in the tuple

print(numbers.index(3)) #Prints the index of the first occurence of 3 in numbers
print(numbers[0]) #Prints the first number of the list

#Unpacking
coordinates = (1, 2, 3) #Creates a tuple that is assigned to variable coordinates
x = coordinates[0]
y = coordinates[1]
z = coordinates[2] #Variables x, y, z are assigned to different values of tuple

x, y, z = coordinates #Easier way of assigning x, y, z to coordinates

print(x) #Prints the value for y as assigned by the coordinates up top
print(y) #This method works for lists as well