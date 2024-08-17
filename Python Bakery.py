# making a robot shopkeeper for a bakery
menu = "1. Plain Cake = 80tk\n"\
       "2. Fruit Cake = 130tk\n"\
       "3. Chocolate Cake = 120tk\n"\
       "4. Marble Cake = 110tk\n"\
       "5. Strawberry Cake = 150tk\n"\
       "6. Banana Cake = 90tk"

print("Hello, Welcome to our bakery shop!!!")
name = input("What is your name?\n")
print("Hello " + name + ", Thank you so much for coming in today!!")
print("Here's what we are serving today:\n", menu)
order = int(input("What would you like to order?\n"))


if (order==1):
    price = 80
    order="Plain Cake"
elif (order==2):
    price = 130
    order = "Fruit Cake"
elif (order==3):
    price = 120
    order = "Chocolate Cake"
elif (order == 4):
    price = 110
    order = "Marble Cake"
elif (order == 5):
    price = 150
    order = "Strawberry Cake"
elif (order == 6):
    price = 90
    order = "Banana Cake"
else:
    print("Sorry, "+ name +". We don't have that today.\nPlease come by some other time. Thank you.")
    exit()

print("Sounds good " + name + ".\nHow many would you like?")
quantity = int(input())
total = quantity * price
print("Your total price is " + str(total) + "\nWe'll have your " + str(quantity) + " " + str(order) + "s ready in a moment!!")
print("Thank you for your purchase, " + name + ".\nPlease visit us again!!")
exit()

