from FindMax import find_max #Importing the FindMax file and then the specific function

numbers = [20, 34, 5, 32, 4, 543] #Create the numbers list that we want to run as our argument
maximum = find_max(numbers) #Assign max to the value of list numbers after it's initialized the function

print(maximum) 
print(max(numbers)) #Use the builtin max function to find the greatest element

