# modified the game
import random
num=random.randint(0,100)
guess=1
n=int(input("guess the number: "))
guess_=False

while not guess_:
    if n==num:
        print(f"The number is correct,and you guessed {guess} times")
        guess_=True
    else:
        if n>num:
            print("Too high")
            guess=guess+1
            n=int(input("guess again: "))
        else:
            print("Too low")
            guess+=1
            n=int(input("guess again: "))
