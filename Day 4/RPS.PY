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
import random
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice >=3 or choice <0:
    print('you selected an invalid number!!!')
else:
    print(game_images[choice])

    computer_choice = random.randint(0,2)

    print(f'computer choose {computer_choice}')

    print(game_images[computer_choice])


    if choice == 0 and computer_choice == 2:
        print('you win!!!')
    elif computer_choice > choice:
        print('you loose!!!!')
    elif choice == computer_choice:
        print('A draw!!!')
    else:
        print('you selected an invalid number.')        