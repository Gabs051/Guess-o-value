# Guess O Value

Welcome to the Guess the Value game, a simple console-based game where you guess a number based on difficulty and a range you set. This game offers two levels of difficulty, and it keeps track of how many attempts you take to guess the correct number.

# Features

- **Two levels of difficulty:**
	 - Easy: The game provides hints if your guess is too high or too low.
	 - Hard: No hints provided, making the game more challenging.
 - **User-defined range for guessing the number.**
 - **Keeps track of the number of attempts made by the user.**
 - **Progess bar indicating score calculation.**

# Getting Started

## *Prerequisites*

 - Python 3.x
 - tqdm library for the progress bar (install using pip install tqdm)

## *How to Run the Game*

 1. Clone or download the repository
 2. Install the required library using: `pip install tqdm`
 3. Run the guess_value.py script: `python guess_value.py`

## Game Flow

 1. Enter yout name.
 2. Choose the difficulty level:<br>
	 2.1. 1 for easy.
	 2.2. 2 for hard.
 3. Enter the range by specifying a minimum and a maximum value:
 4. Start guessing the number! The game will let you know if your guess is within the range.<br>
	 4.1.  In Easy mode, you'll get feedback whether the guess is too high or too low.
	 4.2. In Hard mode, you'll need to guess without any hints.
 5. Once you've guessed the correct number, a progress bar will appear to calculate your score (number of attempts).
 6. Your final score (number of attempts) will be displayed.
## Example Output

    Welcome to the game Guess o Value!!!
    Enter your name: John
    Select difficulty:
    (1)Easy
    (2)Hard
    Difficulty: 1
    Enter a minimum value: 1
    Enter a maximum value: 100
    Enter a value between 1 to 100: 50
    The value is higher...
    Enter a value between 1 to 100: 75
    Congratulations you guessed the value, John!!!, wait a few seconds to see your score...
    
    Calculating: 100%|██████████| 10/10 [00:03<00:00,  3.00it/s]
    
    Here is your score:
    Attempts: 2

## Customization

You can change the range of numbers or difficulty logic by modifying the value_min, value_max, or adding new difficulty levels in the funlevel() function.
