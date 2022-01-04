from replit import clear
#HINT: You can call clear() to clear the output in the console.
biders = {}
add = "yes"
while add == "yes":
  n=input("Enter your name: ")
  b=int(input("Enter the bid amount: "))
  biders[n] = b
  add=input("Is there any other bidder? yes or no ")
  clear()

max_bid=0
bid_name=""
for bid in biders:
  if max_bid < biders[bid]:
    max_bid = biders[bid]
    bid_name = bid

print(f"{bid_name} has won with amount ${max_bid}")