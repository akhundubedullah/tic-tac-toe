#two users
#assign user randomly Cut and Xero or give option to user that this has been selected for user 1 and this has been selected for user 2
#Ask user input for 
#2d arrays to store the inputs
#check if  row  completey matches, so that user wins
# later gui python to integrate
import random



choices = ["X","O"]

Player1 = random.choice(choices)
choices.remove(Player1)
Player2 = random.choice(choices[0])

print("Player 1 has been assigned = ",Player1)
print("Player 2 has been assigned = ",Player2)


