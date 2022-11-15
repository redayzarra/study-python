#Basics
names = ["John", "Bob", "Mosh", "Sam", "Mary"] #Creates a list with names

print(names[0]) #Prints the first element of list with the index of 0
print(names[-1]) #Prints the last element of the list with the index of -1
print(names[-2]) #Prints the second to last element of the list 

names[0] = "Jon" #Changes the first element of the list to the string Jon
print(names)

print(names[0:3]) #Prints elements of index 0 to 3 but not the 3rd one
print(names[2:]) #Prints all elements starting from index of 2 to the end 
print(names[2:4]) #Prints the elements between 0 to 4 but not the 4th one
print(names[:]) #Prints the entire list
print(names) #Does not change the original list

#Practice
numbers = [3, 6, 2, 8, 4, 10, 20] #Creates a list assigned to variable numbers
max = numbers[0] #Assigns the first element to variable max
for number in numbers: #Iterates for every element in numbers
  if number > max: #Runs if the number is greater than the current max
    max = number #Reassigns to the number to a new max if True
print(max) #Prints the value of the highest value in the list

#2D Lists
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
matrix [0] [1] = 20 #First bracket specifies which list, second specifies which element within that list
print(matrix[0] [1]) #Prints the second element in the first list

for row in matrix:
  for item in row:
    print(item)

#List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #Adds a number at the end of the list
numbers.insert(0, -1) #Inserts -1 before the element of index 0, so before the first
numbers.remove(3) #Removes the value 3 from the list
numbers.clear #Removes all the values from the list
numbers.pop() #Removes the last element of the list

numbers.index(5) #Finds the index of the value of 5
numbers.count(2) #Counts the number of times that 2 was in the list

print(1 in numbers) #Returns True if 1 is in the list numbers
print(len(numbers)) #Returns the numbers of elements in a list
numbers.sort() #Sorts the list in ascending order of value
numbers.reverse() #Reverses the list, in this case causes list to be descending
print(numbers)

numbers2 = numbers.copy() #Creates a copy of the list and assigns it to numbers2

#Practice
practice = [1, 2, 3, 3, 4, 5] #Given list with duplicates
uniques = [] #Create an empty list to store our unique list
for number in practice: #Iterate over every element in duplicate's list
  if number not in uniques: #If the number isn't already in the unique list
    uniques.append(number) #Then add it to the list
print(uniques) #Print out the unique list

#List Unpacking
numbers = [1, 2, 3] #Creates a list called numbers that stores 1, 2, and 3

first = numbers[0] #Assigns the variable first to the element at index 0 or the first element
second = numbers[1] #Assigns the variable second to the element at index 1 or the second element
third = numbers[2] #Assigns the variable third to the element at index 2 or the third element

first, second, third = numbers #Automatically assigns the three variables to the indices of 0,1,2
first, second, *other = numbers #Assigns the variables first and second to indices of 0 and 1 while variable other stores the rest of the list
first, *other, last = numbers #Assigns the variable first to the index of 0 and last to the last index, meanwhile other stores everything in between the two
print(first, last) #Prints the variable first and last


#Looping over Lists
letters = ["a", "b", "c"] #Creates a list called letters 
for letter in letters: #Iterates through every element one at a time
  print(letter) #Prints the element as its being iterated through

for letter in enumerate(letters): #Creates a tuple that attaches an index to each element of the list letters
  print(letter) #Prints both the index and letter pair one at a time
  print(letter[0]) #Prints only the indexes of the tuple because they are stored first
  print(letter[1]) #Prints only the element attached to the index
  print(letter[0], letter[1]) #Prints both the index and the element pair

items = [0, "a"] #Creates a list that contains integer 0 and string a
index, letter = items #Assigns the variable index to index 0 and variable letter to index 1
for index, letter in enumerate(letters): #Everytime the for loop iterates, variable index is assigned to the index of the list while letter is assigned to the current element at the time
  print(index) #Only prints the index values of the current loop
  print(letter) #Only prints the letter value of the current loop