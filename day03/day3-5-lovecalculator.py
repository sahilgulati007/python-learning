# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

cnt_true = 0
cnt_true += name1.count('t')
cnt_true += name1.count('r')
cnt_true += name1.count('u')
cnt_true += name1.count('e')

cnt_true += name2.count('t')
cnt_true += name2.count('r')
cnt_true += name2.count('u')
cnt_true += name2.count('e')

cnt_love = 0
cnt_love += name1.count('l')
cnt_love += name1.count('o')
cnt_love += name1.count('v')
cnt_love += name1.count('e')

cnt_love += name2.count('l')
cnt_love += name2.count('o')
cnt_love += name2.count('v')
cnt_love += name2.count('e')

cnt_combine = int(str(cnt_true) + str(cnt_love))

if cnt_combine < 10 or cnt_combine > 90 :
  print(f"Your score is {cnt_combine}, you go together like coke and mentos.")
elif cnt_combine >= 40 and cnt_combine <= 50 :
  print(f"Your score is {cnt_combine}, you are alright together.")
else :
  print(f"Your score is {cnt_combine}.")
