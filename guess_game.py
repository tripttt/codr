n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("You enter less number please input greater number.\n")
        continue
    elif guess_number>18:
        print("You enter greater number please input smaller number.\n ")
        continue
    elif guess_number == 18:
        print("you won\n")
        print(number_of_guesses, "no.of guesses you took to finish.")
        break
    else:
        print("Wrong number")
        print("Game Over!")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
