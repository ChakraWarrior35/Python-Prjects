n = int(input("Enter the number of players:"))
import random

for i in range(n):
    input("Player {}'s turn. Press Enter to roll the dice.".format(i+1))
    dice_roll = random.randint(1, 6)
    print("Player {} rolled a {}".format(i+1, dice_roll))
    if dice_roll == 6:
        print("Congratulations Player {}! You get an extra turn.".format(i+1))
        input("Press Enter to roll the dice again.")
        extra_roll = random.randint(1, 6)
        print("Player {} rolled a {}".format(i+1, extra_roll))
        total = dice_roll + extra_roll
    else:
        total = dice_roll
    print("Player {}'s total score this round is {}\n".format(i+1, total))
print("{}player won the game!".format(random.randint(1, n)))