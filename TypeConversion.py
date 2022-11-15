from datetime import date #import the datetime module to get the current date and time

#Basics
birth_year = input("Enter your birth year: ") #Assigns the variable birth_year as the string on the user's input
todays_date = date.today() #Assign the variable todays_date as the date the current IRL date

age = todays_date.year - int(birth_year) #Assign variable age to be the difference of today's date minus the integer value of variable birth_year

print(age) #Print the value assigned to age

#Definitions
integer_is = 10
float_is = 10.0
bool_is = True or False
str_is = "any kind of words"

#Practice: Make a basic calculator
first_num = float(input("First: "))
second_num = float(input("Second: ")) #Use floats instead of int for decimals

total_sum = first_num - second_num #Assigns the variable total_sum as the difference of first_num minus the second_num
print("Sum: " + str(total_sum)) #Can only concatenate strings with strings