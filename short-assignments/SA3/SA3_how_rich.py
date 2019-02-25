# Author: Thomas Monfre
# Date: 9/22/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program calculates the value of Brutus' wealth based on investment, interest rate, and current year.

# variables set as constants
BRUTUS_INVESTMENT = 1
BRUTUS_INTEREST_RATE = 1.05
CURRENT_YEAR = 2019

# variables
brutus_wealth = 1 # sets initial value of wealth at end of year 1
calculated_year = 1  # keeps track of which year the while loop executes -- assigned to value 2 as start of year 2

while calculated_year <= CURRENT_YEAR:
    brutus_wealth = brutus_wealth * BRUTUS_INTEREST_RATE
    calculated_year = calculated_year + 1

print("At year " + str(CURRENT_YEAR) + ", Brutus' balance is $" + str(brutus_wealth) + ".")