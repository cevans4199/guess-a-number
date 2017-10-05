#Guess a Number AI
#You think of a number, computer tries to get it

#9-25-2017

#Courtney E.



import random

# config
low = 1
high = 100
limit = 7

# helper functions
def show_start_screen():
    print("!$!$!$!$!$!$!$!$!$!$!$!$!$")
    print("$$$$ Guess a Number ! $$$$")
    print("_][_][_][_][_][_][_][_][_")
                                                
def show_credits():
    print("Thanks for playing!This amazing game was created by Courtney Evans.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("Enter a number.")

def pick_number():
    print("I am thinking of a number from " + str(low) + " to " + str(high) +".")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("Dude that's too low!")
    elif guess > rand:
        print("Dude that's too high!")

def show_result(guess, rand):
    if guess == rand:
        print("Lit, you guessed the number!")
    else:
        print("Wow, you're bad at this! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Want to play again?(sure/nah) ")

        if decision == 'sure' or decision == 'yes':
            return True
        elif decision == 'nah' or decision == 'no':
            return False
        else:
            print("Seriously? Just enter 'sure' or 'nah'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
