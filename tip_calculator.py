# tip_calculator revisited - using values provided in a command line list 
# by using the sys module and the sys.argv command

import sys

#brain organization - list values are: 
#sys.argv[0] = tip_calculator.py
#sys.argv[1] = meal
#sys.argv[2] = tax
#sys.argv[3] = tip


#converting list values to floats and converting percents to decimals
meal_float = float(sys.argv[1])
tax_float = float(sys.argv[2]) / 100
tip_float = float(sys.argv[3]) / 100

#further calculations on the cleaned up values
tax_value = (meal_float * tax_float)
meal_with_tax = (meal_float + tax_value)
tip_value = (meal_with_tax * tip_float)

total = (meal_with_tax + tip_value)

#print output values
print "The cost of your meal before tip is $", ("{:.2f}".format(meal_with_tax))
print "$", ("{:.2f}".format(tax_value)), " of that amount is tax"
print "In order to tip", sys.argv[3], "%, you will need to add an additional $", ("{:.2f}".format(tip_value))
print "This will bring the grand total of your meal to $", ("{:.2f}".format(total))




