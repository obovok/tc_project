# tip_calculator revisited exercise

#collecting user input
meal = raw_input("What is the cost of your meal before tax?")
tax = raw_input("What is the tax rate on prepared food?")
tip = raw_input("What percent of your meal cost would you like to leave as tip?")


#converting user input to floats and percents to decimal
meal_float = float(meal)
tax_float = float(tax) / 100
tip_float = float(tip) / 100

tax_value = (meal_float * tax_float)
meal_with_tax = (meal_float + tax_value)
tip_value = (meal_with_tax * tip_float)

total = (meal_with_tax + tip_value)

print "The cost of your meal before tip is $", ("{:.2f}".format(meal_with_tax))
print "$", ("{:.2f}".format(tax_value)), " of that amount is tax"
print "In order to tip", tip, "%, you will need to add an additional$", ("{:.2f}".format(tip_value))
print "This will bring the grand total of your meal to $", ("{:.2f}".format(total))




