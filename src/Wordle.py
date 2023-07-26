import random

from src.utils import print_error, print_success, print_warning

random.seed(42)


class Wordle:
    def __init__(self, file_path, word_len: int = 5, max_count: int = 10_000):
        self.words = self.generate_word_frequency(file_path, word_len, max_count)
        self.word_len = word_len

    def generate_word_frequency(self, file_path, word_len: int, max_count: int):
        words = []
        with open(file_path, "r") as f:
            while True:
                word = f.readline().strip()
                frequency = f.readline()

                if not word or not frequency:
                    break

                frequency = int(float(frequency))
                words.append((word, frequency))

        words = sorted(words, key=lambda w: w[1], reverse=True)
        words = words[:max_count]
        words = [w[0] for w in words]
        words = list(filter(lambda x: len(x) == word_len, words))
        return words

    def run(self, ):
        # Random word
        answer = random.choice(self.words)
        answer = answer.upper()

        #Start game
        num_try = 6
        success = False
        while num_try:
            guess_word = input(f'Enter {self.word_len} letters word (or press q to exit): ')
            guess_word = guess_word.upper()

            # QUIT
            if guess_word.lower() == 'q':
                break

            # Words length
            if len(guess_word) != 5:
                print(f'you entered {len(guess_word)} letter, must entered {self.word_len}')
                continue

            # Check valid word
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid')
                continue

            # Check  valid or invalid positions and invalid characters
            for g_letter,w_letter in zip(guess_word, answer):
                if g_letter == w_letter:
                    print_success(f' {g_letter} ', '')
                elif g_letter in answer:
                    print_warning(f' {g_letter} ', '')
                else :
                    print_error(f' {g_letter} ', '')
            print()

            if guess_word == answer:
                print()
                print_success('Congratulations !!!')
                success = True
                break
            num_try -= 1
        if not success:
            print(f'GameOver:\nThe word was "{answer}".')

