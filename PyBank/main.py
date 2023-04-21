import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
months = 0
net_total = 0
prev_profit_loss = 0
profit_loss_change = 0
max_profit_increase = ['', 0]
max_profit_decrease = ['', 0]

# Open and read the CSV file, skipping the header row
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count the number of months
        months += 1

        # Calculate the net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # Calculate the change in profit/losses
        profit_loss_change = int(row[1]) - prev_profit_loss

        # Keep track of the maximum increase in profits
        if profit_loss_change > max_profit_increase[1]:
            max_profit_increase[0] = row[0]
            max_profit_increase[1] = profit_loss_change

        # Keep track of the maximum decrease in profits
        if profit_loss_change < max_profit_decrease[1]:
            max_profit_decrease[0] = row[0]
            max_profit_decrease[1] = profit_loss_change

        # Keep track of the previous profit/losses
        prev_profit_loss = int(row[1])

# Calculate the average change in "Profit/Losses" over the entire period
average_profit_loss_change = round(net_total / months, 2)

# Print the analysis to the terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_profit_loss_change}")
print(f"Greatest Increase in Profits: {max_profit_increase[0]} (${max_profit_increase[1]})")
print(f"Greatest Decrease in Profits: {max_profit_decrease[0]} (${max_profit_decrease[1]})")


# Initialize csv.writer
output_path = os.path.join("Analysis", "analysis.csv")

with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)

    # Write the analysis in a new CSV file
    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow([f"----------------------------"])
    csvwriter.writerow([f"Total Months: {months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${average_profit_loss_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {max_profit_increase[0]} (${max_profit_increase[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {max_profit_decrease[0]} (${max_profit_decrease[1]})"])