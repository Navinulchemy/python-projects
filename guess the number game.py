import random
print("Welcome to the game")
print("Iam guessing a number from 1 - 100")

def easy_mode():
    guess = random.randint(1, 100)
    print(f"The number to be guessed is {guess}")
    flag = True
    life = 10
    while flag:
        user_guess = int(input("Hey buddy guess a number : "))
        #life = 10
        if user_guess > guess:
            life -= 1
            print("too high")
            print(f"your guess is wrong and remaining life is {life}")
        if user_guess < guess:
            life -= 1
            print("too low")
            print(f"your guess is wrong and remaining life is {life}")

        if user_guess == guess:
            flag=False
            print(f"YOU GUESSED IT CORRECTLY")
        if life == 0:
            flag = False
            print("game over")
    new_game = input("ENTER Y TO start NEW GAME OR TYPE ANY KEY TO QUIT : ").upper()
    if "Y" in new_game:
        difficulty()

def hard_mode():
    guess = random.randint(1, 100)
    print(f"The number to be guessed is {guess}")
    flag = True
    life = 5
    while flag:
        user_guess = int(input("Hey buddy guess a number : "))

        if user_guess > guess:
            life -= 1
            print("too high")
            print(f"your guess is wrong and remaining life is {life}")
        if user_guess < guess:
            life -= 1
            print("too low")
            print(f"your guess is wrong and remaining life is {life}")

        if user_guess == guess:
            flag=False
            print(f"YOU GUESSED IT CORRECTLY")
        if life == 0:
            flag = False
            print("game over")
    new_game = input("ENTER Y TO start NEW GAME OR TYPE ANY KEY TO QUIT: ").upper()
    if "Y" in new_game:
        difficulty()

def difficulty():
      choice = int(input("ENTER 1 FOR EASY MODE AND ENTER 2 FOR HARD MODE: "))
      if choice == 1:
        easy_mode()

      if choice == 2:
        hard_mode()
difficulty()