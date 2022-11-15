#Basics
customer = {
  "name": "John Smith", #Assigns a key to the value 
  "age": 30,
  "is_verified": True #Can use any key to refer to any definition
}
customer["name"] = "Jack Smith" #Can be edited to change the definition to any key
print(customer.get("birthdate", "Jan 1 1980")) #Fetches the definition or assigns it if it doesn't exist

#Practice
phone_num = input("Phone: ") #Create a variable that asks for user input
num_dict = { #Define a dictionary that translates the number to the word
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five", 
  "6": "Six",
  "7": "Seven",
  "8": "Eight",
  "9": "Nine"
}
output = "" #Create an empty output string 
for number in phone_num: #Use this to pass every element of the string through the loop
  output += num_dict.get(number, "!") + " " #Gets the definition associated with each number and then stores it in the ouptut value
print(output)

#Practice
message = input("Type: ") #Asks the user to type a message 
words = message.split(" ") #This function splits the message by a space as indicated
emojis = {
  ":)": "Smile more"
}
output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)