# Braeden Kirby
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

# I can start by converting the values into integer and use a try statement to check if the value can be converted and if it doesn't then the program goes on to check for a float

def value_conversion(v):

    try:

        return int(v)
    
    except ValueError:

        pass

# I have to check to see if the float value has only one decimal so that there isn't an incorrect value

# I also have to count the decimal places within the float

    try:
        
        value_float = float(v)

        if '.' in v:

            if len(v.split('.')[1]) == 1:
                
                return float(v)

            else:

                return False

        else:

            return False
    
    except ValueError:

        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def point_slope_intercept(m, b, lower_x_val, upper_x_val):

    if lower_x_val > upper_x_val:

        return False
    
    y_vals = []

    for x in range(lower_x_val, upper_x_val +1):

        y = m * x + b

        y_vals.append(y)


    return y_vals

while True:

    user_input = input("Please enter a slope (m), a y-intercept (b), a lower bound (x1), and an upper bound (x2) or type 'exit' to quit: ")

    if user_input.lower() == 'exit':

        break

    try: 

        slope_str, intercept_str, lower_str, upper_str = user_input.split()

        m = float(slope_str)

        b = float(intercept_str)

        lower_x_val = int(lower_str)

        upper_x_val = int(upper_str)

        result = point_slope_intercept(m, b, lower_x_val, upper_x_val)

        if result == False:

            print("Invalid value input. Please try again.")

        else:

            print(f"The y-values for x between {lower_x_val} and {upper_x_val} is: {result}")

    except ValueError:

        print("Invalid value input. Please try again")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def sqr_root(x):

    if x < 0:

        return None

    return x ** 0.5

def quadratic_calculator(a, b, c):