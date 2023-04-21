import os
import csv

# Path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}
candidate_percentages = {}
winner = ''

# Open and read the CSV file, skipping the header row
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1

        # If the candidate is not in the dictionary, add them with one vote
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        # Otherwise, add one vote to their existing total
        else:
            candidate_votes[row[2]] += 1

    # Loop through the candidate votes dictionary to calculate their percentages
    for candidate, votes in candidate_votes.items():
        percentage = round((votes / total_votes) * 100, 3)
        candidate_percentages[candidate] = percentage

        # Determine the winner based on popular vote
        if votes == max(candidate_votes.values()):
            winner = candidate

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Initialize csv.writer
output_path = os.path.join("Analysis", "analysis.csv")

with open(output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)

    # Write the analysis in a new CSV file
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    for candidate, percentage in candidate_percentages.items():
        csvwriter.writerow([f"{candidate}: {percentage}% ({candidate_votes[candidate]})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])