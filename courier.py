# Here I am asking the user to input the price and distance of a item they which to buy and get delivered, by using the input() function then storing that data value in a variable called price and dinstance
# I use the float() function to convert the input value to a floating number to ensure accuracy.
price = float(input("Please enter the price of your itme:\n   R"))
distance = float(input("Please enter the distance the courier has to travel in kms:\n   "))

# Here I am then asking the user a few questions the delivery process by using a yes and no type question to determing the factors for each gatagory (transportation metho, if they would like insurance, 
# is the item a gift and if they want priority or standard delivery). I then store those values in variables called "quest1", "quest2", "quest3" and "quest4".
# I use the lower() function here to make sure whatever the user types in is lowercase to make the if and else statemnets process
# easier to code. I save these in new variables called "answer1", "answer2", "answer3" and "answer4"
quest1 = input("Would you like your item to travel by air for R0.25 per km: Yes or no?\n ")
answer1 = quest1.lower()

quest2 = input("Would you like full insurance on your item for R50.00?: Yes or no?\n ")
answer2 = quest2.lower()

quest3 = input("Is this a gift for someone?: Yes or no?\n ")
answer3 = quest3.lower()

quest4 = input("Do you want faster delivery for R100.00 ekstra? otherwise the standard delivery cost will apply of R20.00: Yes or no?\n ")
answer4 = quest4.lower()

# I am also using the if, else statments here to determin the pricing before hand to make the final calculations of the final amount easier on the eye.
# I'm saving these if and else values in new variables called "transport", "insurance", "gift" and "priority"
if answer1 == "yes":
    transport = 0.36
else:
    transport = 0.25

if answer2 == "yes":
    insurance = 50.00
else:
    insurance = 25.00

if answer3 == "yes":
    gift = 15.00
else:
    gift = 0.00

if answer4 == "yes":
    priority = 100.00
else:
    priority = 20.00

# Now with all the variables declared with their respective values accourding to what the user inputted we can finally calculate the total amount the user has to pay for the item.
# This is done by using a simple equastion of addition and multiplication by using the "+" and "*" symbols and then saving that value in the variable called total_amount.
final_tranport = transport * distance
total_amount = price + final_tranport + insurance + gift + priority

# Now we print out a response to the user with their selected options and amounts along with the toal that they have to pay.
# This is done by using the f-string method to add the variables with string data.
print(f"The total amount you have to pay is:\n Item: R{price}\n Transportation: (Method x Travling distance) R{transport} x {distance}km = R{final_tranport}\n Insurance: R{insurance}\n Gift Option: R{gift}\n Delivery fee: R{priority}\n Your total amount due is: R{total_amount}")
