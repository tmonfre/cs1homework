# Author: Thomas Monfre
# Date: 9/22/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program determines the year Brutus' balance exceeds Portia's based on investment & interest-rate.

# variables set as constants
BRUTUS_INVESTMENT = 1.0
BRUTUS_INTEREST_RATE = 1.05
PORTIA_INVESTMENT = 100000.00
PORTIA_INTEREST_RATE = 1.04

# variables
brutus_wealth = BRUTUS_INVESTMENT * BRUTUS_INTEREST_RATE
portia_wealth = PORTIA_INVESTMENT * PORTIA_INTEREST_RATE
year = 1

while brutus_wealth <= portia_wealth:
    brutus_wealth = brutus_wealth * BRUTUS_INTEREST_RATE
    portia_wealth = portia_wealth * PORTIA_INTEREST_RATE
    year = year + 1

print("At year " + str(year) + " Brutus' wealth exceeds Portia's.")

print("Brutus' Wealth: $" + str(brutus_wealth))
print("Portia's Wealth: $" + str(portia_wealth))
