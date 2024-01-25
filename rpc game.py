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

#Write your code below this line 👇
import random
print("What do you choose? \n")
choice = int(input("Type 0 for Rock, 1 for paper or 2 for scissors. \n"))
if choice == 0:
  print(rock)

elif choice == 1:
  print(paper)

elif choice == 2:
  print(scissors)

else:
  print("Invalid input!")
print("Computer chose: \n")
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)

elif computer_choice == 1:
  print(paper)

elif computer_choice == 2:
  print(scissors)

else:
  print("Invalid input!")

if choice == 0 and computer_choice == 1:
  print("You lose!")

elif choice == 0 and computer_choice == 2:
  print("You win!")

elif choice == 2 and computer_choice == 1:
  print("You win!")

elif choice == 1 and computer_choice == 0:
  print("You win!")

elif choice == 2 and computer_choice == 0:
  print("You lose!")

elif choice == 1 and computer_choice == 2:
  print("You lose!")


else:
  print("It's a tie.")




