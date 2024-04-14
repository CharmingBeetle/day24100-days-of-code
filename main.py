import random
print ("Welcome to Infinity dice!")

Sides =  int(input("How many sides?: "))
Play = "yes"

def infdice (Sides):
  print("You rolled", random.randint(1, Sides))
while Play == "yes" or "y":
    infdice (Sides)
    Play = input("Roll again?:")
else:
  print ("Thanks for playing!")




