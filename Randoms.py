import random #Imports the random module

random.random() #Generates a value from 0 to 1

for i in range(3): #Iterate three times
  print(random.random()) #Print the random values
  print(random.randint(10, 20)) #Prints integer values between 10 and 20

members = ["Bob", "Mary", "John", "Me"]
leader = random.choice(members) #Randomly assigns element from members to leader
print(leader)

#Practice
class Dice:
  def roll(self):
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


dice = Dice()
print(dice.roll())