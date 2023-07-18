import csv
import os

file_to_load = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Analysis/budget_analysis.txt"

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
total_net = 0

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)
    
    first_row = next(reader)
    total_months += 1
    #total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        
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
# import csv
# file_to_load = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"
# file_to_output = "C:/Users/shaji/OneDrive/Documents/GitHub/python-challenge/PyBank/Resources/budget_analysis.txt"

# Total_months = 0
# Total = 0
# #profit_avg = 0
# Greatest_Increase_in_profits = ["", 0]
# Greatest_Decrease_in_profits = ["", 99999999999999999]
# months_of_change = []
# profit_change_list = []
# #profit_change = 0
# #row_change_list = []
# #row_change = 0


# with open(file_to_load) as revenue_data:
#     reader = csv.reader(revenue_data)
#     next(reader)
#     first_row=next(reader)
#     header= next(reader)

    
#     Total_months += 1
#     prev_row = int(first_row[1])

#     for row in reader:
#         Total_months += 1
#         row_change = 0
#         Total = Total + int(row[1])

#         #prev_row = int(row[1])
#         profit_change = int(row[1]) - prev_row 
       
        
#         profit_avg = int(row[1]) - prev_row
       
#         profit_change_list = profit_change_list + [row_change]
#         months_of_change = months_of_change + [row[0]]
        
#             #Total_months > 1:
#             #profit_change = int(row[1]) - prev_row
#         profit_change_list+= [profit_change]
#         months_of_change+=[row[0]]

#         if (profit_change > Greatest_Increase_in_profits[1]):
#                 Greatest_Increase_in_profits[0] = row[0]
#                 Greatest_Increase_in_profits[1] = profit_change

#         if (profit_change < Greatest_Decrease_in_profits[1]):
#                 Greatest_Decrease_in_profits[0] = row[0]
#                 Greatest_Decrease_in_profits[1] = profit_change
#         prev_row = int(row[1])
# profit_avg = sum(profit_change_list) / len(profit_change_list)

# output = (
#     f"\nFinancial Analysis\n"
#     f"-------------------------------\n"
#     f"Total Months: {Total_months}\n"
#     f"Total: ${Total}\n"
#     f"Average Change: ${profit_avg}\n"
#     f"Greatest increase in profits: {Greatest_Increase_in_profits[0]} (${Greatest_Increase_in_profits[1]})\n"
#     f"Greatest Decrease in Revenue: {Greatest_Decrease_in_profits[0]} (${Greatest_Decrease_in_profits[1]})\n"
# )

# print(output)

# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)