def prime_checker(number):
  cnt = 0
  for n in range(2,number):
    if number % n==0:
      cnt += 1
  if cnt == 0:
    print("Prime number")
  else:
    print("Not a prime")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)