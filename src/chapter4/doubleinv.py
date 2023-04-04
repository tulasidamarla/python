##
# This program computes the time required to double an investment.
#

# Create constant variables.
RATE = 5.0
INITIAL_BALANCE = 10000
TARGET = 2 * INITIAL_BALANCE

# Initialize variables used with the loop
balance = INITIAL_BALANCE
year = 0

# Count the years required to double the investments.
while balance < TARGET:
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

# Print the results
print("The investment gets doubled after", year, "years")
