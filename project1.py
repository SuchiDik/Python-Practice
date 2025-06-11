'''
1 for snake
-1 for water
0 for gun
'''
import random
'''
computer = random.choice([-1, 0, 1])

user = input("Enter your choice :")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[user]
print(type(you))
# reverseDict = {1: "Snake", -1: "water", 0: "Gun"}
#
# print(f"you chose {reverseDict[you]}\ncomputer chose{reverseDict[computer]}")
if computer == you:
    print("It's a draw")

else:
    if computer == -1 and you == 1:
        print("You win")
    elif computer == -1 and you == -0:
        print("You lose")
    elif computer == 1 and you == -1:
        print("You lose")
    elif computer == 1 and you == 0:
        print("You win")
    elif computer == 0 and you == -1:
        print("You win")
    elif computer == 0 and you == 1:
        print("You lose")
    else:
        print("Something went wrong")
'''

# Import random module
import random
print('Snake - Water - Gun')


# Input no. of rounds
n = int(input('Enter number of rounds: '))


# List containing Snake(s), Water(w), Gun(g)
options = ['s', 'w', 'g']

# Round numbers
rounds = 1

# Count of computer wins
comp_win = 0

# Count of player wins
user_win = 0


# There will be n rounds of game
while rounds <= n:

    # Display round
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

    # Exception handling
    try:
        player = input("Choose your option: ")
    except EOFError as e:
        print(e)

    # Control of bad inputs
    if player != 's' and player != 'w' and player != 'g':
        print("Invalid input, try again\n")
        continue

    # random.choice() will randomly choose
    # item from list- options
    computer = random.choice(options)
    print(f"computer chose {computer}")
    # Conditions based on the game rule
    if computer == 's':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1

    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1

    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1

    # Announce winner of every round
    if user_win > comp_win:
        print(f"You Won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer Won round {rounds}\n")
    else:
        print("Draw!!\n")

    rounds += 1


# Final winner based on the number of wons
if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")