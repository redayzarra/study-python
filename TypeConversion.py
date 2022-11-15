#import the datetime module to get the current date and time 
from datetime import date

#Basics
birth_year = input("Enter your birth year: ") #Returns the value as a string
todays_date = date.today() #Ass

age = todays_date.year - int(birth_year)

print(age)

#Definitions
integer_is = 10
float_is = 10.0
bool_is = True or False
str_is = "any kind of words"

#Practice: Make a basic calculator
first_num = float(input("First: "))
second_num = float(input("Second: ")) #Use floats instead of int for decimals

total_sum = first_num - second_num

print("Sum: " + str(total_sum)) #Can only concatenate strings with strings
