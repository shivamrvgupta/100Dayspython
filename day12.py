################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

# Guess the Number


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from replit import clear
from art import logo
import random

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, number,turns):
  if guess > number:
    print("Too high.")
    return turns - 1
  elif guess < number:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {number}.")

def set_difficulties():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_TURNS
  elif level == "hard":
    return HARD_TURNS
  else: 
    print("Enter the proper value")
    clear()
    return game()

    
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  number = random.randint(1,100)
  print(number)

  turns = set_difficulties()
  guess = 0

  while guess != number:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess : "))
    turns = check_answer(guess, number, turns)
    
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:  
      print("Guess Again")
      
game()