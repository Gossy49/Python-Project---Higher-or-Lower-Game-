from art import logo,vs
from game_data import data
import random


#keep user score
current_score = 0

game = True


#print B
game_art = print (logo)

        #get the name, description and country

a_choice = random.choice (data)
a_followers = a_choice ['follower_count']
a_compare = (f'Compare A:  {a_choice['name']}, {a_choice['description']}, {a_choice['country']} ')
print (a_compare)

game_art2 = print (vs)


b_choice = random.choice (data)
b_followers = b_choice['follower_count']
b_compare = f'Compare B:  {b_choice['name']}, {b_choice['description']}, {b_choice['country']} '
print(b_compare)




while game : 
#get user's answer

    
    user_answer = input ("who has more followers? Type 'A' or 'B':  ")

    if user_answer == 'A' and a_followers > b_followers:

        current_score += 1
        print (f"You're correct! Current score: {current_score}.")
        print(a_compare)

        game_art2 = print (vs)

        b_choice = random.choice (data)
        b_followers = b_choice['follower_count']
        b_compare = f'Compare B:  {b_choice['name']}, {b_choice['description']}, {b_choice['country']} '
        print(b_compare)

        



    elif user_answer == 'B' and b_followers > a_followers:
        current_score +=1
        print (f"You're correct! Current score: {current_score}.")
        a_choice = b_choice
        a_compare = (f'Compare A:  {a_choice['name']}, {a_choice['description']}, {a_choice['country']} ')

        print (a_compare)

        game_art2 = print (vs)

        b_choice = random.choice (data)
        b_followers = b_choice['follower_count']
        b_compare = f'Compare B:  {b_choice['name']}, {b_choice['description']}, {b_choice['country']} '
        print(b_compare)


        
    else:
        print(f"Sorry, that's wrong. Final score {current_score}")
        game = False


        