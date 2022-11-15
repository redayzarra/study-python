#Basics
course = "Python for Beginners" #Assigns the value in quotes to variable courses

print(course.upper()) #Runs the value of course through a model to uppercase letters
print(course) #The command above is returning a new string

print(course.find("y")) #Returns the index of the first time y is spotted in value
print(course.find("Y")) #Returns -1 because capital Y doesn't exist
print(course.find("for")) #Returns 7 because that's the index of the word for

print(course.replace("for", "4")) #Replaces for with the string after the coma
print(course.replace("x", "y")) #Nothing changes because x doesn't exist

print(course.find("Python")) #Returns the index of the word Python which is 0
print("Python" in course) #Checks to see if the word Python is in variable course

