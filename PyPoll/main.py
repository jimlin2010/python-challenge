import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   #print(f"CSV Header: {csv_header}")

    index = 0
    value = 0
    votes = 0
    winner = ""
    candidate_dict = {}
    max = 0


    for row in csvreader:
        index += 1

        if row[2] in candidate_dict:
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1

    print("Election Results")
    print("-------------------------")

    print(f'Total Votes: {index}')
    print("-------------------------")

    for canname, value in candidate_dict.items():
        print (f"{canname}: {round(value/index*100,3)}% ({value})")
        if value > max:
            max = value
            winner = canname
    print("-------------------------")
    print (f"Winner: {winner}")
    print("-------------------------")




    
