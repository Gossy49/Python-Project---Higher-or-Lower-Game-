from art import logo 
from game_data import data
import random

#game_art = print (logo)



#get the name, description and country

a_choice = random.choice (data)
a_ccompare = print(f' Compare A:  {a_choice['name']}, {a_choice['description']}, {a_choice['country']} ')



#get user's answer
#user_answer = input ("who has more followers? Type 'A' or 'B' ")