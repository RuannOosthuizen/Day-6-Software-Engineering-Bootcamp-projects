# Here I am asking the user if they are a salesperson or a manager to determine the equetion needed for the calculations for their monthly wages.
# This is done by using a input function then saving that data value in a variable called question.
question = input("Please state your position at the department?\n(salesperson or manager): ")

# Then by using the .lower() function to change the letters all lowercases for easier use later on in the if and else statements. I save this value in a variable called title.
title = question.lower()

# Here I am using the if and nested if statements to ask the user in thei respective psotion, what is their sales gross for a salesperson or hours worked for a manager.
# then saving that data in a new variable called gross or hours. This is then used to determing their wages by using mutliplication "*" and addition "+" symbols which is then saved in variables called
# sales_wage or manager_wage
# to calculate their final amount of wages.
# I use the float() and itn () function here for more accurate measurements of the data and to cast the string data to an int or float data type for the calculations to work.
if title == "salesperson":
    gross = float(input("Please enter the total amount of gross sales this month?\n :R"))
    sales_wage = gross * 0.08 + 2000.00
    print(f"This employees wage as salesperson is R{sales_wage} this month.")
# Here I use the round() function for just incase the use puts in a none integer as we only need the hours worked to calculate the final amount.
elif title == "manager":
    hours = round(int(input("Please enter the hours you have worked this month?\n :Hr ")))
    manager_wage = 40.00 * hours
    print(f"This employees wage as manager is R{manager_wage} this month.")