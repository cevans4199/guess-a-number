#Guess a Number AI
#You think of a number, computer tries to get it

#9-25-2017

#Courtney E.


# config
low = 1
high = 1000

# helper functions
def show_start_screen(): 
    print ("  ____  __ __    ___  _____ _____      ____      ____   __ __  ___ ___  ____     ___  ____        ____  ____ ")
    print (" /    ||  |  |  /  _]/ ___// ___/     /    |    |    \ |  |  ||   |   ||    \   /  _]|    \      /    ||    |")
    print ("|   __||  |  | /  [_(   \_(   \_     |  o  |    |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )    |  o  | |  | ")
    print ("|  |  ||  |  ||    _]\__  |\__  |    |     |    |  |  ||  |  ||  \_/  ||     ||    _]|    /     |     | |  | ")
    print ("|  |_ ||  :  ||   [_ /  \ |/  \ |    |  _  |    |  |  ||  :  ||   |   ||  O  ||   [_ |    \     |  _  | |  | ")
    print ("|     ||     ||     |\    |\    |    |  |  |    |  |  ||     ||   |   ||     ||     ||  .  \    |  |  | |  | ")
    print ("|___,_| \__,_||_____| \___| \___|    |__|__|    |__|__| \__,_||___|___||_____||_____||__|\_|    |__|__||____|")                                                                                                          



def show_credits():
    print("   ____           _____                 _                      ______                      ")
    print("  |  _ \         / ____|               | |                    |  ____|                     ")
    print("  | |_) |_   _  | |     ___  _   _ _ __| |_ _ __   ___ _   _  | |____   ____ _ _ __  ___   ")
    print("  |  _ <| | | | | |    / _ \| | | | '__| __| '_ \ / _ \ | | | |  __\ \ / / _` | '_ \/ __|  ")
    print("  | |_) | |_| | | |___| (_) | |_| | |  | |_| | | |  __/ |_| | | |___\ V / (_| | | | \__ \  ")
    print("  |____/ \__, |  \_____\___/ \__,_|_|   \__|_| |_|\___|\__, | |______\_/ \__,_|_| |_|___/  ")
    print("         __/ |                                         __/ |                               ")
    print("        |___/                                         |___/                                ")

     
def get_guess(current_low, current_high):
    g = (current_high + current_low) // 2
    print(g)
    return g
    

def pick_number():
    print ("Think of a number between " + str(low)+ " and " + str(high) + ".")
    input ("Hit that enter button to continue")

def check_guess(guess):
    print ("Was my number too high, too low, or correct?")
    answer = input()
    if answer.lower() == "too high" or answer.lower() == "l":
        return 1
    elif answer.lower() == "too low" or answer.lower() == "h":
        return -1
    elif answer.lower() == "correct" or answer.lower() == "c":
        return 0
    else:
        print ("I dont understand. Please enter too high, too low, or correct.")
            
def show_result():
    print ("Lit, I got it!")


def play_again():
    while True:
        decision = input("You want to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
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
            current_low = guess
        elif check == 1:
            current_high = guess

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



