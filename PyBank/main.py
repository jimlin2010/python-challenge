# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    total_months = 0
    total_profit = 0
    cur_profit = 0
    previos_profit = 0
    delta_profit = 0
    change_profit = 0
    avechange_profit = 0
    delta = [] 
    max_profit_increase = 0
    max_profit_decrease = 0
    maxinc_date = ''
    maxdec_date = ''


    # Read each row of data after the header
    for row in csvreader:

        int_profit = int(row[1])
        # add the profit/losses of cur month to total profit
        total_profit += int_profit
        previos_profit = cur_profit
        cur_profit = int(row[1])
        if total_months < 1:
            delta_profit = 0
        else:
            delta_profit = cur_profit - previos_profit

        if max_profit_increase < delta_profit:
            max_profit_increase = delta_profit
            maxinc_date = row[0]
        if max_profit_decrease > delta_profit:
            max_profit_decrease = delta_profit
            maxdec_date = row[0]
        
        change_profit +=delta_profit

        total_months += 1

    avechange_profit = change_profit / (total_months-1)

        # calculate each delta here, if cur delta is larger than max_profit_increase, update max_profit_increase
        # if cur delta is smaller than max_profit_decrease, update max_profit_decrease

    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total months: {total_months}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${round(avechange_profit, 2)}')
    print(f'Greatest Increase in Profit: {maxinc_date} (${max_profit_increase})')
    print(f'Greatest Increase in Profit: {maxdec_date} (${max_profit_decrease})')

    # calculate ur avg change here: add all ur delta val and divide by total_months



        
