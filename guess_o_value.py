#importing libraries that we will use
from random import randint
from time import sleep
from tqdm import tqdm

print(f'\033[1;36mWelcome to the game Guess o Value!!!\033[m')
user = str(input('\033[1;32mEnter your name: \033[m'))

level = int(input('\033[1;36mSelect difficulty:\n\033[1;32m(1)Easy\n\033[1;31m(2)Hard\n\033[1;36mDifficulty: \033[m'))
#user will enter a value according to the difficulty they want and will go through a check
while level <= 0 or level > 2:
    print('\n\033[1;33mThere was an error choosing a value, enter again...')
    level = int(input('\033[1;36mSelect difficulty:\n\033[1;32m(1)Easy\n\033[1;31m(2)Hard\n\033[1;36mDifficulty: \033[m'))

value_min = int(input('\033[1;36mEnter a minimum value: \033[m'))
value_max = int(input('\033[1;36mEnter a maximum value: \033[m'))
counter = 0
machine_value = randint(value_min, value_max)

while True:
    user_value = int(input(f'\033[1;36mEnter a value between {value_min} to {value_max}: \033[m'))

    #checking if the value is within the range that the user wanted
    while user_value < value_min or user_value > value_max:
        print('\n\033[1;33mThere was an error choosing a value, enter again...\033[m')
        user_value = int(input(f'\033[1;36mEnter a value between {value_min} to {value_max}: \033[m'))

    counter += 1

    if level == 1:
        if user_value < machine_value:
            print('\n\033[1;37mThe value is higher...\033[m')
        elif user_value > machine_value:
            print('\n\033[1;37mThe value is smaller...\033[m')
        elif user_value == machine_value:
            print(f'\n\033[1;32mCongratulations you guessed the value, {user}!!!, wait a few seconds to see your score...\033[m')
            break

    if level == 2:
        if user_value == machine_value:
            print(f'\n\033[1;32mCongratulations you guessed the value, {user}!!!, wait a few seconds to see your score...\033[m')
            break

#progress bar
for i in tqdm(range(10), desc="\033[1;36mCalculating"):
    sleep(0.3)

print(f'\n\033[1;36mHere this your scores:\nAttempts: \033[1;32m{counter}\033[m')
