#######################################################################################################################################################
# 
# Name: Shyam Balachandar
# SID: 750021288
# Exam Date: 28/03/2025
# Module: BEMM458
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-sb1557  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences
# Taking the exact key-value pair for the keywords dictionary
ref_sid = [keywords[7], keywords[8]]

# Initialize the dictionary to store keyword counts
keyword_counts = {i: 0 for i in ref_sid}

# Process the customer reviews to count keyword occurrences
for j in customer_reviews.split():
    j = j.strip(".,").lower()  # Clean punctuation and make lowercase
    if j in keyword_counts:
        keyword_counts[j] += 1

# Print the results
print("Keyword counts:", keyword_counts)


##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here: 75
# Insert last two digits of ID number here: 88

# Exact values based on your ID number (75 and 88)
revenue = 75
cogs = 88
avg_inventory = 75
start_customers = 75
end_customers = 88
new_customers = 7
fixed_costs = 75
selling_price = 88
variable_cost = 7

# Write your function for Gross Profit Margin
def gross_profit_margin(revenue, cogs):
    margin = ((revenue - cogs) / revenue) * 100
    return margin

# Write your function for Inventory Turnover
def inventory_turnover(cogs, avg_inventory):
    turnover = cogs / avg_inventory
    return turnover

# Write your function for Customer Retention Rate (CRR)
def customer_retention_rate(start_customers, end_customers, new_customers):
    retained_customers = end_customers - new_customers
    crr = (retained_customers / start_customers) * 100
    return crr

# Write your function for Break-even Analysis
def break_even_analysis(fixed_costs, selling_price, variable_cost):
    break_even_units = fixed_costs / (selling_price - variable_cost)
    return break_even_units

# Calling my functions here
#printing the Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), Break-even Analysis
print("Gross Profit Margin:", gross_profit_margin(revenue, cogs), "%")
print("Inventory Turnover:", inventory_turnover(cogs, avg_inventory))
print("Customer Retention Rate (CRR):", customer_retention_rate(start_customers, end_customers, new_customers), "%")
print("Break-even Point (Units):", break_even_analysis(fixed_costs, selling_price, variable_cost))


##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Actual Data declaration
delivery_cost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
shipment_volume = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250])

# inserting values for slope, intercept, r_value, p_value, std_err 
slope, intercept, r_value, p_value, std_err = linregress(delivery_cost, shipment_volume)

# Predicting the  shipment volume for £68
predicted_volume = slope * 68 + intercept
print(f"Predicted shipment volume for a cost of £68: {predicted_volume:.2f} units")

# Calculate optimal delivery cost to maximize profit
# Assume profit = (Revenue - Cost), where Revenue = Volume * Selling Price (e.g., £100 per unit)
selling_price = 100  # Example selling price per unit
profits = []

for cost in delivery_cost:
    volume = slope * cost + intercept
    revenue = volume * selling_price
    profit = revenue - (volume * cost)
    profits.append(profit)

optimal_cost = delivery_cost[np.argmax(profits)]
optimal_profit = max(profits)
print(f"Optimal delivery cost to maximize profit: £{optimal_cost}")
print(f"Maximum profit: £{optimal_profit:.2f}")

# Plotting the regression line and data points
plt.scatter(delivery_cost, shipment_volume, color='blue', label='Data Points')
plt.plot(delivery_cost, slope * delivery_cost + intercept, color='red', label='Regression Line')
plt.xlabel('Delivery Cost (£)')
plt.ylabel('Shipment Volume (Units)')
plt.title('Linear Regression: Delivery Cost vs Shipment Volume')
plt.legend()
plt.show()


##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

#Here the importing of random module is wrong. Instead of import radom, its written as import rand as random
# import rand as random
# import matplotlib.pyplt as plt

# # Generate 100 random numbers between 1 and student ID number
# your_ID=input("Enter your Student ID: ")
# max_value = int(your_ID)

#The variable max_value is not properly declared here and the in range function also not declared properly.
#the your_ID variable is used inside the randint function which expects integers.
# random_numbers = [random.randint(your_ID, max_valu) in range(100)]

# # Plotting the numbers in a histogram
#instead of using plt.hist, it has been declared as plt.histogram
#Used bin instead of bins
#Used colour instead of color
# plt.histogram(random_number, bin=10, edgecolour='blue', alpha=0.7, colour='red')
# plt.title="Histogram of 100 Random Numbers"
#Used = instead of parenthesis for xlabel
# plt.xlabel="Value Range"
#Used = instead of parenthesis for ylabel
# plt.ylabel="Frequency"
# plt.grid("True")
#Used plt.show("plot") instead of plt.show()
# plt.show("plot")


#Commented the mistakes above and written the corrected code below.


import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number
your_ID = input("Enter Student ID: ")
max_value = int(your_ID)

random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a histogram
plt.hist(random_numbers, bins=10, edgecolor='blue', alpha=0.7, color='red')
plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()