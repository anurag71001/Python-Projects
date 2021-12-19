n = 18
z = 1
while(z<=9):
    guess_number = int(input("Guess the number : "))
    if guess_number > 18:
        print("Oops!! you've entered the larger number. Please Enter the "
              "smaller number.\n")
        print("only", 9-z, "guesses left.\n")
        z += 1

    elif guess_number < 18:
        print("Oops!! you've entered the smaller number. Please enter the "
              "larger number.\n")
        print("only", 9 - z, "guesses left.\n")
        z += 1
    else:
        print("Congrats!! You've guessed the correct number and you won the "
              "game.")
        print("You took only", z, "guesses.")
        z += 1
        break
    if z > 9:
        print("GAME OVER!!\nYou have lost all your guesses")