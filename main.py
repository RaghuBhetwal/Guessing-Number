import random
randNum = random.randint(1, 100)  # Random number from 1 to 100
print(randNum)

userGuess = None
guesses = 0
while (userGuess != randNum):   #loop until you guess correct int
    userGuess = int(input("Enter your guess number: "))
    guesses += 1
    if (userGuess == randNum):
        print("Your guess is right!!")
    else:
        if (userGuess < randNum):
            print("Your Guess is wrong. Enter a Larger number!!")
        else:
            print("Your Guess is wrong. Enter a Smaller number!!")
print(f"You guessed the Number in {guesses} attempt")

with open("hiscore.txt", "r") as f:       # Storing least number of attempts
    hiscore = int(f.read())
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write("Your best attempts:")
        f.write(str(guesses))