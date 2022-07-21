from random import random
from art import logo,logo2 
from poplist import insta_dict
import random

# accessing names  of popular guys on ig

def any_name():
    '''get a random name'''
    name = random.choice(list(insta_dict))
    return name
first_person = any_name()
second_person = any_name()

def num_of_followers(name):
    '''get the number of followers each star chosen at random has'''
    if name in insta_dict:
        ig_follow = insta_dict[name]
        return ig_follow
    else:
        return None

def find_highest_followers(any_choice):
    if any_choice == 'A':
        if A > B:
            return True
        else:
            return False 
    elif any_choice == 'B':
        if B > A:
            return True
        else:
            return False
    else:
        print('wrong input') 

print(logo)




score = 0
game_end = False

while  not game_end:
    first_person = any_name()
    second_person = any_name()
    A = num_of_followers(first_person)
    B = num_of_followers(second_person)
    print(f'Compare A: {first_person} ')
    print(logo2)
    print(f'Against B: {second_person}')
    choice = input("Who has more followers? type 'A' or 'B': ").lower()
    if find_highest_followers(choice) == True:
        score+=1
        print(f'You are right, current score: {score}.')
    else:
        print(f'You are wrong, current score : {score}')
        game_end = True   