import random as rn

def NumGuessGame():
    print("<< Welcome To Guess Number Game \U0001f601 >>\n")

    while True:
        res = int(input("1 => to Read Rules\n2 => to Start the Game\n Your Answer : "))
        if res == 1:
            print("--------------------------------------------------------------------------------------------------------------\nRules:\nThis is Just a Simple Game, All you need is to guess the Target number\nYou have 10 attempts to guess, \nif the number u choose is greater than the Target number --Displaying--> 'The target number is less than your guess.'\nif is less than --Displaying--> 'The target number is greater than your guess.' \nEnjoy it !!\n--------------------------------------------------------------------------------------------------------------")
        elif res == 2:
            break
        else:
            print("--------------------------------------------------------------------------------------------------------------\nError(InputInvalid): Try to input a Valid Number\n--------------------------------------------------------------------------------------------------------------")

    while True:
        # Initialize counter of attempts and the right number;
        Level = int(input("-----------------------------------{ Difficulty Level }-----------------------------------\n1-easy\n2-medium\n3-hard\n Your answer: "))
        if Level == 3:
            N=300
        elif Level == 2:
            N = 100
        elif Level == 1:
            N = 50
            
        TargetNum = rn.randint(1, N)
        Attempts = 10

        # Start the game
        print("-----------------------------------{ Game Started }-----------------------------------")
        print("Guess the number between 1 and %d.\n--------------------------------------------------------------------------------------------------------------" % N)
        while Attempts > 0:
            print("You have %d Attempts left:" % Attempts)
            num = int(input("\nEnter your guess: "))

            if num == TargetNum:
                print("--------------------------------------------------------------------------------------------------------------")
                print("Congratulations! You've guessed the correct number:", TargetNum)
                print("--------------------------------------------------------------------------------------------------------------")
                break
            elif num < TargetNum:
                print("--------------------------------------------------------------------------------------------------------------")
                print("The target number is greater than your guess.\n")
                print("--------------------------------------------------------------------------------------------------------------")
            else:
                print("--------------------------------------------------------------------------------------------------------------")
                print("The target number is less than your guess.\n")
                print("--------------------------------------------------------------------------------------------------------------")

            Attempts -= 1

        if Attempts == 0:
            print("Game Over. \U0001F923")
            print("The Target number was:", TargetNum)

        playAgain = input("Do you want to play again? (yes/no): ")
        if playAgain.lower() != "yes":
            break
        
        print("\n")

# Call the function to start the game
NumGuessGame()
