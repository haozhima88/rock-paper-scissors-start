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
your_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
list_c = [rock, paper, scissors]
print(list_c[your_chose])

computer_chose = random.randint(0,2)
print(f"Computer chose:{list_c[computer_chose]}")

if your_chose == 0:
  if computer_chose == 0:
    print("Try again")
  elif computer_chose == 1:
    print("You lose")
  elif computer_chose == 2:
    print("You Win")
elif your_chose == 1:
  if computer_chose == 0:
    print("You Win")
  elif computer_chose == 1:
    print("Try again")
  elif computer_chose == 2:
    print("You lose")
elif your_chose == 2:
  if computer_chose == 0:
    print("You lose")
  elif computer_chose == 1:
    print("You Win")
  elif computer_chose == 2:
    print("Try again")