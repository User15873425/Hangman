import random
import sys


def correct(answer):
    global life
    if len(answer) != 1:
        print('Please, input a single letter.')
        return False
    elif not answer.islower():
        print('Please, enter a lowercase letter from the English alphabet.')
        return False
    elif answer in guessed_letters:
        print("You've already guessed this letter.")
        return False
    else:
        guessed_letters.add(answer)
    if answer not in hidden:
        life -= 1
        print(f"That letter doesn't appear in the word.  # {life} attempts")
        return False
    return True


def game(word):
    global hint
    global score
    while life > 0:
        letter = input(f'\n{hint}\nInput a letter: ')
        if correct(letter):
            index = [i for i, j in enumerate(word) if j == letter]
            for _ in range(word.count(letter)):
                x = index.pop()
                hint = hint[:x] + letter + hint[x+1:]
            if hint.count('-') == 0:
                print(f'\nYou guessed the word {word}!\nYou survived!')
                score['win'] += 1
                menu()
    if life == 0:
        print('You lost!')
        score['lose'] += 1
        menu()


def menu():
    global hidden
    global guessed_letters
    global hint
    hidden = random.choice(words)
    guessed_letters = set()
    hint = '-' * len(hidden)
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choice == 'play':
        game(hidden)
    elif choice == 'results':
        print(f'You won: {score["win"]} times\nYou lost: {score["lose"]} times')
        menu()
    elif choice == 'exit':
        sys.exit()


words = ('python', 'java', 'swift', 'javascript')
hidden = random.choice(words)
guessed_letters = set()
hint = '-' * len(hidden)
life = 8
score = {'win': 0, 'lose': 0}

print('H A N G M A N  # 8 attempts')
menu()
