import csv
import os

# import files and create file to export
file_to_load = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Analysis/budget_analysis.txt"

# Name variables
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

# Open file
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

#Label header row
    header = next(reader)
    
    # skip first row
    first_row = next(reader)

    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        #calculations
        total_months += 1
        total_net += int(row[1])
        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
       
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)
# Results
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
