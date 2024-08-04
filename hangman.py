import random
#you can change the words
words = ['python', 'laptop', 'action', 'wheather']
word = random.choice(words)
guesses = '-' * len(word)
attempts = 8

while attempts > 0:
    print(guesses)
    guess = input("Input a letter: ")

    if guess in word:
        new_guesses = ''
        for i in range(len(word)):
            if word[i] == guess:
                new_guesses += guess
            else:
                new_guesses += guesses[i]
        guesses = new_guesses
    else:
        attempts -= 1
        print(f"That letter doesn't appear in the word. Attempts left: {attempts}")

    if '-' not in guesses:
        print(f"You guessed the word {word}!")
        print("You survived!")
        break
else:
    print("You lost!")
#danialtla
