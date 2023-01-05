# Import the math module.
import math

# Display the two types of finance calculator and its detail to the user.
print("investment - to calculate the amount of interest you'll earn on your investment"
      "\nbond - to calculate the amount you'll have to pay on a home loan.\n")

# User enters their choice of finance calculator.
finance_calculator = input("Choose either 'investment' or 'bond' from the menu to proceed: ")

# If the user enters 'investment', print 'You have selected investment'.
# The program then asks user to input required deposit amount, interest rate and time needed for calculating investment.
if finance_calculator.lower() == "investment":
    print("You have selected 'Investment'!")
    deposit_amount = float(input("Please enter the amount you are depositing: "))
    interest_rate = float(input("Please enter the rate of interest (%): "))
    time = int(input("Please enter the number of years you plan on investing: "))

    # Convert the 'interest_rate' to percentage by dividing it by 100 and store it in the variable 'rate'.
    rate = interest_rate / 100

    # User chooses their preferred interest type (simple or compound).
    interest = input("Please choose interest type (Simple / Compound): ")

    # If the interest chosen is 'simple', use the simple interest formula to calculate the total_amount and print it.
    # The simple interest used formula is: A = P (1 + r * t)
    # where A = total_amount, P = deposit_amount, r = rate and t = time
    if interest.lower() == "simple":
        total_amount = deposit_amount * (1 + rate * time)
        print(f"The Simple Interest is: {round(total_amount,2)}")

    # Else, the user chose compound, use the compound interest formula to calculate the total_amount and print it.
    # The compound interest formula used is: A = P (1 + r) ^ t 
    else:
        total_amount = deposit_amount * math.pow(1 + rate, time)
        print(f"The Compound Interest is: {round(total_amount,2)}")


# Else, if the user enters 'bond', print 'You have selected bond'.
elif finance_calculator.lower() == "bond":
    print("You have selected 'Bond'!")

    # The program then asks user to input house value, interest rate and time needed for calculating bond.
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the rate of interest: "))
    time = int(input("Please enter the number of months you plan to take to repay the bond: "))

    # Convert the interest_rate to percentage by dividing it by 12 (months) and 100 and store it in the variable 'rate'.
    rate = interest_rate / 1200

    # Calculate the bond using the formula and print message appropriately.
    # The bond formula is: x = (i * P) / (1 - ( 1 + i) ^ (-n))
    # where x = bond, i = rate and n = time
    bond = (rate * house_value) / (1 - (1 + rate) ** (-time))
    print(f"Amount to be repaid each month: {round(bond,2)}.")

# Otherwise, if the user doesn't type 'investment' or 'bond', use else statement to display error message.
else:
    print("Error! Invalid input entered!")



