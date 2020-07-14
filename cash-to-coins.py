# Create a function that will take all your coins and convert it to the cash amount.

def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    dollars = 0
    for key, value in coins.items():
        if key == 'pennies':
            dollars += value * 0.01
        elif key == 'nickels':
            dollars += value * 0.05
        elif key == 'dimes':
            dollars += value * 0.10
        else: 
            dollars += value * 0.25
    print(dollars)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)