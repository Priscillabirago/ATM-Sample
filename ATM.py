# the initial amount of money in the user's account is $500
account = int(500)
# user inputs their name
name = input("Enter your name")
# user enters their account number
number = int(input("Enter account number"))
# user enters the amount the want to withdraw
amount = int(input("Enter amount to be withdrawn"))
# amount to be withdrawn is deducted if it is less than or equal to $500 and balance is calculated
if amount <= 500:
    print("Hello " + name + ". Your transaction of " + str(amount) + " cedis has been successful and your current balance is " + str(account - amount))
# user is unable to redraw money if it is more than $500
else:
    print("Hello " + name + ". You cannot withdraw more than your available balance.")
