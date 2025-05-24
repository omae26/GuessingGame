# We specify a secret word and the user will keep guessing until they get the secret word right
# 23/05/2025

secret_word = "giraffe"  # A variable that will store the secret word
guess = ""   # A variable to store the user's guess
guess_count = 0  # A variable to store/track the number of times the user has guessed
guess_limit =  3 # How many times the user can guess the word
out_of_guesses = False #Boolean var. Whether or not the user is out of guesses. True = out of guesses. False = stil some guesses

while guess != secret_word  and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ") # when guess is not the secret word
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else: 
    print ("You win!") 

# Allowing the user to guess as many times as possible until they get the secret word
# Setting a limit  to the number of guess