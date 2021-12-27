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

#Write your code below this line 👇
arr = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_choice = random.randint(0, 2)


if user_choice <0 or user_choice >2 :
  print("Enter correct choice")
else :
  print ("user choice is" + arr[user_choice])
  print ("Comp choice is" + arr[comp_choice])
  if user_choice == 0 and comp_choice == 2:
    print("You Win")
  elif user_choice ==2  and comp_choice == 0:
    print("COMP Win")
  elif user_choice == comp_choice :
    print("Its a draw")
  elif user_choice < comp_choice :
    print("Computer Win")
  elif comp_choice < user_choice :
    print("You Win")