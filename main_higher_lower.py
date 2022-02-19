from random import *
import os
from art import logo, vs
from game_data import data


#______________________________________
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

#______________________________________

def main_higher_lower(score = 0, first = choice(data), second = choice(data)):
	first_p = first
	second_p = second
	total_score = score

	clear_screen()
	print(logo)

	if total_score > 0:
		print(f"You're right! Current score: {total_score}")
		first_p = second_p
	second_p = choice(data)

	print(f"Compare A: {first_p['name']}, a {first_p['description']}, from {first_p['country']}.\n{vs}")
	print(f"Against B: {second_p['name']}, a {second_p['description']}, from {second_p['country']}")

	guess = input("Who has more followers? Type 'A' or 'B': ")
	more_followers = compare(first_p, second_p)

	if guess == 'A' and more_followers == "first" or guess == 'B' and more_followers == "second":
		total_score += 1
		main_higher_lower(total_score, first_p, second_p)
	else:
		print("You're Loose!")

		if input("Repeat? 'y' or 'n': ")== 'y':
			main_higher_lower(0, choice(data), choice(data) )
		else:
			print("Good bye!")


#______________________________________

def compare(first, second):
	if first['follower_count'] > second['follower_count']:
		return "first"
	else:
		return "second"

#_______________________________________

main_higher_lower()


