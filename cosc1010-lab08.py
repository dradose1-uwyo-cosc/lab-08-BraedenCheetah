# Braeden Kirby
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to: Matthew Curl, Austin Barner
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def value_converter(num):

    isNegative = False

    if "-" in num:

        isNeg = True

        num = num.replace("-", "")
    
    if "." in num:

        num_list = num.split(".")

    if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():

        if isNegative:

            return -1 * float(num)

        else:

            return float(num)
            
    elif num.isdigit():

        if isNegative:

            return -1 * int(num)

        else:

            return False

    else:

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

# I can start by making it so the lower bound is checked to be less than the upper bound and returns as an invalid value if it is mroe than the upper bound

def point_slope_intercept(m, b, lower_x_val, upper_x_val):

    if lower_x_val > upper_x_val:

        return False
    
    y_vals = []

    for x in range(lower_x_val, upper_x_val +1):

        y = m * x + b

        y_vals.append(y)

# I can make it so that there is the equation that is produced and used to find the upper and lower bounds

    return y_vals

while True:

    user_input = input("Please enter a slope (m), a y-intercept (b), a lower bound (x1), and an upper bound (x2) (put a space between each input value) or type 'exit' to quit: ")

    if user_input.lower() == 'exit':

        break

# I can use the try statment to help me separate the parts out and assign individual values to each

    try: 

# I can turn the 'm' and 'b' into floats and the bounds into integers so that they are applicable in the program

        slope_str, intercept_str, lower_str, upper_str = user_input.split()

        m = float(slope_str)

        b = float(intercept_str)

        lower_x_val = int(lower_str)

        upper_x_val = int(upper_str)

# I can set the result to be the result of the equation and have it calculate the bounds for me

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

# I can create a def for the square root operation and make it so the return is 'None' for if the input value is less than zero

def sqr_root(x):

    if x < 0:

        return None

    return x ** 0.5

# I can then make a def for the quadratic function calculator I want and use the previous square root to add it into the equation

def quadratic_calculator(a, b, c):

    equation = b ** 2 - 4 * a * c

    sqr_rt_equation = sqr_root(equation)

    if sqr_rt_equation is None:

        print("The equation has complex roots.")

        return None, None
    
    root_1 = (-b + sqr_rt_equation) / (2 * a)

    root_2 = (-b - sqr_rt_equation) / (2 * a)

    return root_1, root_2

# I can make a while loop to have the user input the values they wish and change the roots into usable variables

# Making sure that they are float numbers and work well makes it so they are able to be ran in the code

while True:

    try:

        a = float(input("To start the Quadratic Equation, please enter a value (non-zero) for 'a': "))

        if a == 0:

            print("Please try again. 'a' must be a non-zero for the quadratic equation")

            continue

        b = float(input("Enter the value of 'b': "))
        
        c = float(input("Enter the value of 'c': "))

        root_1, root_2 = quadratic_calculator(a, b, c)

        if root_1 is not None:

            print(f"The roots of the equation are: {root_1} and {root_2}")

        else:

            print("No Solutions. There is no solution that satisfies the input values.")

        continuation = input("Would you like to continue with another euqation? (yes/no): ").strip().lower()

        if continuation != 'yes':

            break

    except:

        print("Invalid value. Please try again.")