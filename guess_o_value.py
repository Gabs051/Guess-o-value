import random

print(f'Welcome to the game Guess o Value!!!')
user = str(input('Enter your name: '))

level = int(input('\nSelect difficulty:\n(1)Easy\n(2)Hard\nDifficulty: '))
while level <= 0 or level > 2:
    print('There was an error choosing a value, enter again...')
    level = int(input('\nSelect difficulty:\n(1)Easy\n(2)Hard\nDifficulty: '))

value_min = int(input('\nEnter a minimun value: '))
value_max = int(input('Enter a maxinum value: '))
counter = 0
machine_value = random.randint(value_min, value_max)

while True:
    user_value = int(input(f'\nEnter a value between {value_min} to {value_max}: '))
    
    while user_value < value_min or user_value > value_max:
        print('There was an error choosing a value, enter again...')
        user_value = int(input(f'Enter a value between {value_min} to {value_max}: '))
    
    counter += 1
    
    if level == 1:
        if user_value < machine_value:
            print('\nThe value is higher...')
        elif user_value > machine_value:
            print('\nThe value is smaller...')
        elif user_value == machine_value:
            print(f'\nCongratulations you guessed the value, {user}!!!, wait a few seconds to see your score...')
            break
    
    if level == 2:
        if user_value == machine_value:
            print(f'\nCongratulations you guessed the value, {user}!!!, wait a few seconds to see your score...')
            break

print(f'Here this your scores:\nAttempts: {counter}')
