#Basics
for x in range(4): #Creating a range from 0 to 4 while excluding 4
  for y in range(3): #Creating a range from 0 to 3 while excluding 3
    print(f"({x}, {y})") #Will continue until inner loop completes

#Practice
numbers = [1, 1, 1, 1, 4]

for x_count in numbers:
  output = ''
  for count in range(x_count):
    output += "x"
  print(output)