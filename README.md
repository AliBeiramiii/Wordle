# Wordle

wordle is a word game, which become popular nowadays.
Limits are omitted in this version, you can play as many as you want and customize it.

## Rules

- The player enters random five-letter word.
- Player has 6 guesses to win (only meaningful words count)
- There are 3 stages:
    1. green: the letter and its position is right.
    2. yellow: only the letter is correct.
    3. red: none of the letters or positions are not correct.

## How to Run

- Clone the repository and `cd` into it.
- Install the requirements by running `pip install -r requirements.txt`.
- In your terminal, run `export PYTHONPATH=$PYTHONPATH:$(pwd)` to add the current directory to your `PYTHONPATH`.
- Run `python src/wordle.py` to start the game.
