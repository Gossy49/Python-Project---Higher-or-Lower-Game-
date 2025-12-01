from art import logo,vs
from game_data import data
import random


#keep user score
current_score = 0


#print B
game_art = print (logo)



#get the name, description and country

a_choice = random.choice (data)
a_followers = a_choice ['follower_count']
a_ccompare = print(f'Compare A:  {a_choice['name']}, {a_choice['description']}, {a_choice['country']} ')

game_art2 = print (vs)


b_choice = random.choice (data)
b_followers = b_choice['follower_count']
b_compare = print(f'Compare B:  {b_choice['name']}, {b_choice['description']}, {b_choice['country']} ')

#get user's answer
user_answer = input ("who has more followers? Type 'A' or 'B':  ")

if user_answer == 'A' and a_followers > b_followers:
    current_score += 1
    print (f"You're correct! Current score: {current_score}.")

elif user_answer == 'B' and b_followers > a_followers:
    a_ccompare = b_compare
    current_score +=1
    print (f"You're correct! Current score: {current_score}.")
    
else:
    print(f"Sorry, that's wrong. Final score {current_score}")


        