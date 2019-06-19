import os
import csv

month_count = 0
total_revenue = 0
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

# open csv file
with open(r'C:\Users\engmo\Desktop\PREWORK_MIQ\Module-3\budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # looping for getting monthly changes in revenue and getting month counts
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[1])
        total_revenue = total_revenue + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue

# calculating the month to month results
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index +1]
min_month = months[min_month_index +1]

# print summary to on python
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

# save summary to txt
output_path = os.path.join(r'C:\Users\engmo\Desktop\PREWORK_MIQ\Module-3\New_data.txt')

with open(output_path,'w', newline='') as txtfile:
    
    
    txtfile.write("Financial Analysis\r\n" )
    txtfile.write("----------------------------------------\r\n")
    txtfile.write(f"Total Months: {month_count}\r\n")
    txtfile.write(f"Total Revenue: ${total_revenue}\r\n")
    txtfile.write(f"Average Revenue Change: ${average_change}\r\n")
    txtfile.write(f"Greatest Increase in Revenue: {max_month} (${max_change})\r\n")
    txtfile.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})\r\n")
