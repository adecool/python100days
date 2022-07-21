#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
EASY_LEVEL = 'easy'
HARD_LEVEL = 'hard'
random_num = random.randint(1,101)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

levels_choice = input("choose a difficulty. Type 'easy' or 'hard': ")
user_guess = int(input("enter a guess between 1 and 100: "))
#print(random_num)
def number_of_turns():
  if levels_choice == EASY_LEVEL:
    turns = 10
    return turns
  else:
    turns = 5
    return turns
turns = number_of_turns()
is_guess_right = False
while turns != 0 and not is_guess_right:
  turns -=1
  if user_guess > random_num:
    print('Too high')
    print('guess again.')
    print(f"you have {turns} attempts remaining to guess the number.")  
    user_guess = int(input("enter a guess between 1 and 100: "))

  elif user_guess < random_num:
    print('Too low')
    print('guess again.')
    print(f"you have {turns} attempts remaining to guess the number.")  
    user_guess = int(input("enter a guess between 1 and 100: "))
  else:
    print(f"you guessed right, the number is {user_guess}")
    is_guess_right = True
  print("You've run out of guesses, you loose.")
  