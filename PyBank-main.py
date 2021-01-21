# Homework 3 Python Challenge 

#Import Dependencies 
import os 
import csv 

# Include Variables to set amounts 
total_months=0 
net_amount=0 
monthly_change=[]
month_count=[]
greatest_increase=0 
greatest_increase_month=0 
greatest_decrease=0 
greatest_decrease_month=0 

# Set Path For File 
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Open & Read CSV File 
    with open(csvpath, newline= "") as csvfile:

#csv Reader Specifies the delimiter & Variable that holds the contents 
    csvreader= csv.reader(csvfile, delimiter= ".")

#Header Row will be read first (If there is no Header Skip)
    csv_header= next(csvreader)
    row = next(csvreader)

#Calculate Total Number of Months, Net Amount of "Profit/Losses" and set Variables for Rows 
previous_row = int(row[1])
total_months +=1
net_amount += int(row[1])
greatest_increase = int(row[1])
greatest_increase_month = row[0]

#Read Row of data after Header 
for row in csvreader:

    #Calculate Total Number of Months
    total_months += 1
    #Amount of "Profit/Losses" over the entire period 
    net_amount += int(row[1])

    #Calculate Change from Current Month to Previous Month 
    revenue_change = int(row[1]) - previous_row 
    monthly_change.append(revenue_change)
    previous_row = int(row[1])
    month_count.append(row[0])

    #Calculate the Greatest Increase 
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        greatest_increase_month = row [0]

    #Calculate the Greatest Decrease
    if int(row[1])< greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_month= (row[0])

    #Calculate the Avg & the Date 
    average_change = sum(monthly_change)/len(monthly_change)
    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print Data 
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_amount}")
print(f"Average Change: {average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month},({highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month},({lowest})")

#Revised File 
output_file = os.path.join(".", "PyBank", "Resources", "budget_data_revised.text")

#OPEN REVISED FILE 
with open(output_file, "w,") as txtfile:

#Print New Data 
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"--------------------")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total:{net_amount}\n")
    txtfile.write(f"Average Change: {average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month},({highest})")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month},({lowest})")
