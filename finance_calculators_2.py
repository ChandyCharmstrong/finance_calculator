#Choose a calculator. Bond/Investment 

import math

I_or_B = input("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \n \nEnter either 'investment' or 'bond' from the menu above to proceed:")
I_or_B = I_or_B.lower()
print(I_or_B)
if I_or_B == "bond" or I_or_B == "investment":
    print("Proceeding to", I_or_B, "calculator.")
else:
    print("To access a caluclator, please refresh and enter either 'Investment' or 'Bond'.")

# For the following formuala, Simple = A = P * (1 +r*t):
# P = Initial deposit 
# r = Interest Rate 
# t = Time 
# A = Final amount (Including interest) 

if I_or_B == "investment":
    P = int(input("Please enter initial deposit value (£):"))
    r = int(input("Please enter interest rate (number only):"))/100
    t = int(input("Please enter the number of years you would like to invest for:"))
    interest = input("Please enter interest type: 'Simple' or 'Compound':")
    interest = interest.lower()
    if interest == "simple":
        A = P * (1 + r * t)
        print("Total amount with simple interest: £", A)
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print("Total amount with compound interest: £")
    else:
        print("Invalid interest type specified.")

# For the following formuala, Compound = A = P * math.pow((1+r),t):
# P = Present house value 
# i = Monthly interest rate 
# n = number of months over which the bond will be repayed 

if I_or_B == "bond":
    P = int(input("Please enter the present house value: (£)"))
    i = int(input("Please enter the annual interest rate (number only)"))/100
    n = int(input("Over how many months would the bond be repaid:"))
    A = (i * P)/(1 - (1 + i)**(-n))
    print("Your total repayment value is: £", A)