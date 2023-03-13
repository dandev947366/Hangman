from random import choice
from time import sleep

print("Hello! Welcome to Hangman game \n")
name = input("Enter your name: ")
print("Nice to meet you " + name + "\n") , sleep(1)
print("Game Start \n")

def main():
    global count
    global word
    global display
    global guessed

    count = 0
    word = choice(["mother","passion","eternity","fantastic","destiny","liberty","peace","sunshine","hope","grace","blue"])
    display = '_' * len(word)
    guessed = []

def hangman():
    global count
    global word
    global display
    global guessed

    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    if guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    
    elif len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try to input a letter \n")
        
    elif guess in guessed:
        print("Letter already exist, Try another letter\n")

    else:
        count += 1
        if count == 1:
            print("   ___ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining \n")

        elif count == 2:
            print("   ___ \n"
                  " |     | \n"
                  " |     | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining \n")

        elif count == 3:
           print("   ___ \n"
                 " |     | \n"
                 " |     | \n"
                 " |     | \n"
                 " | \n"
                 " | \n"
                 " | \n"
                 "_|_\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining \n")

        elif count == 4:
            print("   ___ \n"
                  " |     | \n"
                  " |     | \n"
                  " |     | \n"
                  " |     O \n"
                  " | \n"
                  " | \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guess remaining \n")

        elif count == 5:
            print("   ___ \n"
                  " |     | \n"
                  " |     | \n"
                  " |     | \n"
                  " |     O \n"
                  " |    /|\ \n"
                  " |    / \ \n"
                  "_|_\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:" , guessed , word , "\n")

    if word == '_' * len(word):
        print("Congrats! You have guessed the word correctly! \n")
    
    elif count != limit:
        hangman()

main()
hangman()
play_game = input("Do You want to play again? y = yes, n = no \n")

while play_game not in ["y","n","Y","N"]:
    play_game = input("Do You want to play again? please type: y = yes, n = no \n")

while play_game in ["y" , "Y"]:
    main()
    hangman()
    play_game = input("Do You want to play again? y = yes, n = no \n")

if play_game in ["n" or "N"]:
    print("Thank you for playing!")
