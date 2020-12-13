import time
from random import seed
from random import randint
name = input("What is your name?\n")
print (f"Hello, {name}")

time.sleep (1)
print ("Welcome to 'Guess that Number'!")
time.sleep (1)

while True:
        print ("Random Number is being generated...")
        time.sleep (0.2)
        print (".")
        time.sleep (0.2)
        print (".")
        time.sleep (0.2)
        print (".")

        number = randint(0, 100)

        print ("Done!")
        count = 0

        input ("press Enter to continue")


        while True:
                
                guess = int(input ("Please enter your guess (must be an integer)\n"))
                count +=1
                if guess > number:
                        print ("Woops, it's not that, try lower \n")
                elif guess < number:
                	print ("Woops, it's not that, try higher\n")
                elif guess == number:
                        break
                else:
                        print ("That's not an integer you fool!")

        print ("Congratulations! You win!")
        print (f"You only needed {count} tries!")
        while True:
                play = input ("Would you like to play again (y/n)\n")
                if play == "y":
                        break
                elif play == "n":
                        raise SystemExit
                else:
                    print (f"Invalid input, {name}")
                    pass
        




