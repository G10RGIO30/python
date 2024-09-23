from datetime import datetime

base_greeting = "Hello"
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")
name = input("What is your name? ")

greeting = base_greeting + " " + name + " Today is " + formatted_date + " Welcome to currency exchange service"
print(greeting)

dollars = float(input("How many dollars do you have? "))
euros = dollars * 0.88

ten_euro_bills = euros // 10
remaining_amount = euros - ten_euro_bills * 10
one_euro_bills = remaining_amount // 1
remaining_amount = remaining_amount - one_euro_bills
euro_coins = remaining_amount

print("You'll get " + str(euros) + " euros.")

print("Ten euro bills: " + str(ten_euro_bills))
print("One euro bills: " + str(one_euro_bills))
print("Euro coins: " + str(euro_coins))

print("Thanks for using currency exchange service " + name)