#Basic Guessing Game


secret_word = "Happiness"
guess = ""
attempt = 0
attempt_limit = 3
out_of_guesses = False


#promt the user to enter their guess
#if they guess wrong, prompt again

while guess != secret_word and not (out_of_guesses):
    if attempt < attempt_limit:
        guess = input("Enter Guess: ")
        attempt += 1
    else:
         out_of_guesses  = True

if out_of_guesses:
    print("You are out of attempts")
else:
    print(f"You guessed it! the secret word was " + secret_word)

