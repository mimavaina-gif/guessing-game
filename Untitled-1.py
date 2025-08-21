def guess_game():
    print("             Welcome To The Guessing Games")
    print("Guess The Number From 1 To 100 To Win 1 Million Dollars")
    print("                    (Not Actually)...")
    print("=======================================================")
    while True:
        ready_to_play = input("                 Ready To Play?: ").strip().lower()
        if ready_to_play == "yes":
            print("                Let The Games Beging!")
            print("=======================================================")
            break
        elif ready_to_play == "no":
            print("Oh")
            print("Too Bad")
        else:
            print("=======================================================")
            print("                        Huh?")
            print("=======================================================")
    while True:
        print("                  Pick Difficulty")
        print("                        Hard")
        print("                       Normal")
        print("                        Easy")
        difficulty = input("                Choose: ").strip().lower()
        print("=======================================================")
        if difficulty == "hard":
            amount_of_tries = 4
            print("                  You Get 5 Tries")
            break
        elif difficulty == "normal":
            amount_of_tries = 9
            print("                 You Get 10 Tries")
            break
        elif difficulty == "easy":
            amount_of_tries = 14
            print("                 You Get 15 Tries")
            break
        else:
            print("                        Huh?")
            print("=======================================================")
    import random
    num = random.randint(0, 100)
    guess = 0
    while True:
        guess = input("     Enter Your Choice: ")
        if not guess.isdigit():
            print("              Please Enter A Number")
            continue
        guess = int(guess)
        if guess == num:
            print("                      WINNER")
            print("        You Got It On Your First Attemp!!!")
        elif guess > num:
            print("                    Guess Lower")
            print("=======================================================")
            break
        elif guess < num:
            print("                    Guess Higher")
            print("=======================================================")
            break
        else:
            break
    tries = 1
    while tries <= amount_of_tries:
        guess = input("             Try Again: ")
        if not guess.isdigit():
            print("               Please Enter A Number")
            continue
        guess = int(guess)
        if guess == num:
            tries = tries + 1
            print("                      WINNER")
            print("               You Got It In " + str(tries) + " Tries!")
            break
        if guess > num:
            print("                    Guess Lower")
            print("=======================================================")
            tries = tries + 1
        if guess < num:
            print("                    Guess Higher")
            print("=======================================================")
            tries = tries + 1
        if tries == amount_of_tries:
            print("                  Ran Out Of Tries")
            print("                     Game Over")
            print("                    Answer Was " + str(num))
            print("               Better Luck Next Time")
            break
guess_game()
while True:
    play_again = input("Want To Play Again?: ").strip().lower()
    if play_again == "yes":
        print("Okay!")
        guess_game()
    elif play_again == "no":
        print("oh.")
        print("ok.")
        break
    else:
        print("Huh?")
        