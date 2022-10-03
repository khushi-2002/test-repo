#Blind auction program
from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art 

print(art.logo)
print("Welcome to the secret auction program")
result_dic={}
flag=True
while flag:

  name = input("What's your name? ")
  bid = int(input("What is your bid? $"))
  result_dic[name]=bid
  choice = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  if choice=="no":
    flag=False
  else:
    clear()

highest_bid=0
for amount in result_dic:
  if highest_bid < result_dic[amount]:
    highest_bid=result_dic[amount]
    winner=amount
    
print(f"According to the highest bid: Auction winner is {winner} with {highest_bid}")    
