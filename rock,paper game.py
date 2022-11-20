import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
while True:
 usr_inp = int(input("Enter 0 for rock 1 for paper 2 for scissors :"))
 if usr_inp > 2 or usr_inp < 0:
    print("invalid choice try again")
 else:
    print(game[usr_inp])
    comp_inp = random.randint(0, 1)
    print(game[comp_inp])
    if usr_inp == comp_inp:
        print("both are equal try another time")

    elif usr_inp == 0 and comp_inp == 1:
        print("you lose")
    elif usr_inp == 0 and comp_inp == 2:
        print("you win")
    elif usr_inp == 1 and comp_inp == 0:
        print("you win")
    elif usr_inp == 1 and comp_inp == 2:
        print("you lose")
    elif usr_inp == 2 and comp_inp == 0:
        print("you lose")
    elif usr_inp == 2 and comp_inp == 1:
        print("you win")