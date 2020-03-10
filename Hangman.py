# Hangman By Corey
import random
# Set up an array to keep track of player guesses and compare to the correct word
animal = ['cat','bat', 'dog', 'mouse', 'rabbit', 'moose', 'bearcat', 'bear', 'kangaroo', 'wolf', 'tiger', 'lion', 'monkey', 'donkey', 'horse', 'bird', 'fox', 'bobcat', 'crocodile', 'cow', 'pig', 'frog', 'toad', 'coyote', 'deer', 'cougar'  ]
winCon = 0

rananimal = random.choice(animal)
underscores = []
for character in rananimal:
    underscores.append('_')

# Counter and max tries
tries = 0
loser = 5

# Loops the game until the player is finished
finished = False
while not finished:
    print(f'You have {loser - tries} tries left.')
    stringUnderscores = ' '.join(underscores)
    print(f'Can you guess this animal???? : {stringUnderscores}')


# The hangman drawing
    print('  []--------[|]    ')
    print('  []         \     ')
    print('  []         '+('(x.x)' if tries > 1 else ''))
    print('  []         '+('(|*|)' if tries > 2 else ''))
    print('  []         '+(' | |  ' if tries > 3 else ''))
    print('  []         '+(' 0 0  ' if tries > 4 else ''))
    print('__||_________'+('GAME OVER!!!!' if tries > 5 else ''))


# Player input for letter
    guess = input('Enter your guess of each letter in the animals name one letter at a time: ')


    if guess in rananimal:
        for i in range(len(rananimal)):

            character = rananimal[i]
            if character == guess:
                underscores[i] = rananimal[i]
                winCon += 1

    else:
        print(f'Incorrect input! {guess} is not in this animals name')
        tries += 1

    if winCon == len(rananimal):
        print(f'GOOD WORK! You guessed the animal I was thinking of.')
        finished = True

    if tries >= loser:
        print(f'YOU FAILED!!')
        finished = True






