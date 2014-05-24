# tip_calculator revisited - using values from ConfigParser

import ConfigParser

config = ConfigParser.ConfigParser()
#note: i do not know what the above line is for

config.read("tip.ini")

#converting list values to floats and converting percents to decimals
meal_float = float(config.get("first_round", "meal"))
tax_float = float(config.get("first_round", "tax")) / 100
tip_float = float(config.get("first_round", "tip")) / 100

#test the above
#print meal_float
#print tax_float
#print tip_float



#further calculations on the cleaned up values
tax_value = (meal_float * tax_float)
meal_with_tax = (meal_float + tax_value)
tip_value = (meal_with_tax * tip_float)

total = (meal_with_tax + tip_value)

#print output values
print "The cost of your meal before tip is $", ("{:.2f}".format(meal_with_tax))
print "$", ("{:.2f}".format(tax_value)), " of that amount is tax"
print "In order to tip", config.get("first_round", "tip") , "%, you will need to add an additional $", ("{:.2f}".format(tip_value))
print "This will bring the grand total of your meal to $", ("{:.2f}".format(total))




