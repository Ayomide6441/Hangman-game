import random
from level import level, logo
from words import word_list


print(logo)
game_ended = False
lives = len(level) - 1

random_word = random.choice(word_list)
word_length = len(random_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_ended:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess_letter not in random_word:
        print(
            f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_ended = True
            print("You lose, try again")

    if not "_" in display:
        game_ended = True
        print("Good job! You win.")
    print(level[lives])
