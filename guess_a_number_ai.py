# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    g = (current_high + current_low) // 2
    return g
    

def pick_number():
    print ("Think of a number between " + str(low) + " + str(high) + ".")
    input ("Press enter to continue")

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

def show_result():
    if guess = "correct"
    print ("Lit, I got it!")
else:
    print ("Dang, Ill get it next time!")


def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision.lower == 'y' or decision.lower == 'yes':
            return True
        elif decision.lower == 'n' or decision.lower == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            guess= current_low
        elif check == 1:
            guess= current_high

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



