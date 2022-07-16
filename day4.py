# Head or Tails 


import random
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")





# Banker Roulette

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)

random_name = random.randint(0, num_items - 1)

payer = names[random_name]

print(f"{payer} is going to buy the meal today!")

# Tresure Map 

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

hori = int(position[0])
verti = int(position[1])

map[hori - 1][verti - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Rock paper and scissor

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

if user_choice < 0 and user_choice >= 3:
  print("invalid number")
elif user_choice == 0 and computer_choice == 2:
  print("you wins, computer lose")
elif user_choice == 2 and computer_choice == 0:
  print("you lose, computer wins")
elif user_choice  > computer_choice:
  print("you win, computer lose")
elif user_choice  < computer_choice:
  print("you lose, computer win")
elif user_choice == computer_choice:
  print("It's a draw")