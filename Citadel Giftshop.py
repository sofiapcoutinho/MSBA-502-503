#Sofia Pereira Coutinho
#September 16, 2022

#This program will handle the checkout process for The Citadel's Giftshop.

#The program will prompt the customer for a name.
name = input("Hello, welcome to The Citadel's Giftshop! Can I get a name for the order? ")
print()

#The variable plumbuses is a string that determines whether the customer wants to buy the product.
#The variable plumbuses_number is an integer that determines how many plumbuses the customer wants. The default is 0, unless the customer specifies they want this product.
plumbuses = input(str(name) + ", would you like to buy any Plumbuses? (yes or no) ")
plumbuses_number = 0

#The customer is prompted to answer "yes" or "no" to whether they would like the first product, plumbuses.
#If "yes", they must input how many, which affects the variable plumbuses_number. The code will let them know the number they specified.
#The program recognizes the three most common types of capitalization. Otherwise it will default to "No".
if plumbuses == "No" or plumbuses == "no" or plumbuses == "NO":
    print("Okay,", name, "no plumbuses.")
elif plumbuses == "Yes" or plumbuses == "yes" or plumbuses == "YES":
    plumbuses_number = int(input("How many Plumbuses would you like to buy? "))
    print("Great,", plumbuses_number, "plumbuses!")
else:
    print("Oops! Looks like a typo. We'll treat that as a no.")
print()

#The variable total determines the amount the customer will have to pay at the end, based on the discounts available per quantity.
#The default for total is 0, because the default for plumbuses_number is 0. 
if plumbuses_number <5:
    total = plumbuses_number * 20
elif plumbuses_number < 15:
    total = plumbuses_number * 17.5
else:
    total = plumbuses_number *15.25


#The program will run the equivalent code for the second product, Meeseeks Boxes.
meeseeks =  input("Would you like to buy any Meeseeks Boxes, " + str(name) + "? (yes or no) ")
meeseeks_number = 0
if meeseeks == "No" or meeseeks == "no" or meeseeks == "NO":
    print("Alright, no Meeseeks Boxes.")
elif meeseeks == "Yes" or meeseeks == "yes" or meeseeks == "YES":
    meeseeks_number = int(input("How many Meeseeks Boxes would you like to buy? "))
    print(meeseeks_number, "Meeseeks Boxes it is!")
else:
    print("Oops! Looks like a typo. We'll treat that as a no.")
print()

#The variable total will add itself with the amount the customer owes for the second product.
if meeseeks_number < 10:
    total += meeseeks_number * 1.75
elif meeseeks_number < 18:
    total += meeseeks_number * 1.5
else:
    total += meeseeks_number * 1.25


#The program will run the equivalent code for the third product, Portal Fluid.
#The variable portal_fluid_number is a float, because it can be a decimal, unlike the previous two products.   
portal_fluid =  input("Finally, would you like to buy any Portal Fluid? (yes or no) ")
portal_fluid_number = 0
if portal_fluid == "No" or portal_fluid == "no" or portal_fluid == "NO":
    print("Okay, " + str(name) + ", no Portal Fluid.")
elif portal_fluid == "Yes" or portal_fluid == "yes" or portal_fluid == "YES":
    portal_fluid_number = float(input("How many gallons of Portal Fluid would you like to buy? "))
    print("Alright " + str(name) + ", " + str(portal_fluid_number) + " gallons of Portal Fluid!")
else:
    print("Oops! Looks like a typo. We'll treat that as a no.")
print()

if portal_fluid_number < 3:
    total += portal_fluid_number * 8
elif portal_fluid_number < 7:
    total += portal_fluid_number * 7
else:
    total += portal_fluid_number * 6

#The program will print what the customer has in their cart, based on what they have specified they wanted to purchase.
if plumbuses_number == 0:
    if meeseeks_number == 0:
        if portal_fluid_number == 0:
            print("Your cart is empty.")
        else:
            print("You have", portal_fluid_number, "gallons of Portal Fluid in your cart.")
    elif portal_fluid_number == 0:
        print("You have", meeseeks_number, "Meeseeks Boxes in your cart.")
    else:
        print("You have", meeseeks_number, "Meeseeks Boxes, and", portal_fluid_number, "gallons of Portal Fluid in your cart.")
elif meeseeks_number == 0:
    if portal_fluid_number == 0:
        print("You have", plumbuses_number, "plumbuses in your cart.")
    else:
        print("You have", plumbuses_number, "plumbuses, and", portal_fluid_number, "gallons of Portal Fluid in your cart.")
else:
    if portal_fluid_number == 0:
        print("You have", plumbuses_number, "plumbuses, and", meeseeks_number, "Meeseeks Boxes in your cart.")
    else:
        print("You have", plumbuses_number, "plumbuses;", meeseeks_number, "Meeseeks Boxes; and", portal_fluid_number, "gallons of Portal Fluid in your cart.")


#The program will print the running total amount that the customer owes.
print(str(name) + ", your final total is " + str(total) + " dollars.")
print()
print("Thanks for visiting The Citadel's Giftshop! We hope to see you again soon.")
