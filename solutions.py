"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    money = input("What is your total sales?")
    print('Profit: $' + format(int(money) * 0.23, ",.2f"))


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    int1 = input("What is your first int?")
    int2 = input("What is your second int?")
    print(int2 + " goes into " + int1 + " a total of " + str(int(int(int1)/int(int2))) + " times with a remainder of " + str(int(int1) % int(int2)))


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles = input("Num of miles driven")
    gallons = input("Num of gallons of gas used")
    print("Miles driven: " + miles + "/n")
    print("Gas used (gallons): " + gallons + "/n")
    print("Miles per gallon: " + str(int(miles)/int(gallons)))


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1 = format(float(input("What is price 1?")), ".2f")
    price2 = format(float(input("What is price 2?")), ".2f")
    price3 = format(float(input("What is price 3?")), ".2f")
    price1 = format(str(price1), ">20s")
    price2 = format(str(price2), ">20s")
    price3 = format(str(price3), ">20s")
    print("Here are your prices! \n")
    print("\n")
    print("Price #1: $ " + price1 + "\n")
    print("Price #2: $ " + price2 + "\n")
    print("Price #3: $ " + price3 + "\n")


