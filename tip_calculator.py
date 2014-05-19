# tip_calculator revisited exercise

meal = 17.0
tax = .0825
tip = .2

tax_value = (meal * tax)
meal_with_tax = (meal + tax_value)
tip_value = (meal_with_tax * tip)

total = (meal_with_tax + tip)

print "Your meal costs $", ("{:.2f}".format(meal_with_tax))
print "$", ("{:.2f}".format(tax_value)), " of that amount is tax"
print "In order to tip 20%, your tip amount should be: $", ("{:.2f}".format(tip_value))
print "The grand total of your meal (including tax and tip) is: $", ("{:.2f}".format(total))




