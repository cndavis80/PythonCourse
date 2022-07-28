import random

computer_choice = random.choice(["rock", "paper", "scissors"])

user_choice = input('Do you want -rock, paper, or scissor?\n')

if user_choice == random.choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == "scissors":
    print('WIN')
elif user_choice == 'paper' and computer_choice == "rock":
    print('WIN')
elif user_choice == 'scissors' and computer_choice == "paper":
    print ('WIN')
else:
   print('Computer wins :D')


