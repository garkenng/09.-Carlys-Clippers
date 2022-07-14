"""
Carlys Clippers a fictional hair salon
"""

from statistics import mean

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Average price of a haircut at Carlys Clippers
total_price = 0

for price in prices:
    total_price += price

# Average price equals total number of elements in the prices list via the len
average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(round(average_price,2)))

# Instead of using len to calculate the average. Can use the mean function from Statistics module.
# Produces the same reuslt as average_price
mean_price = mean(prices)
print("Mean Prices: $" + str(round(mean_price,2)))

# Using list comprehension, reduce all prices by $5 into a new list called new_prices
new_prices = [pri - 5 for pri in prices]
# Display new prices
print("New Price List" + str(new_prices))

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(total_revenue))

# Calcualtes the average daily takings
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Prints out haircuts which are $30 or below using list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] <= 30]
# Prints hairstyles but which square brackets and comma
print("Hairsytles which cost $30 or less: " + str(cuts_under_30))
# Prints as a list with no symbols
for i in cuts_under_30:
    print(i)