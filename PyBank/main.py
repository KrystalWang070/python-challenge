import os
import csv

csvpath = os.path.join('Resource','budget.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Set the requested variables as integers and strings
    
    month = 0
    net_profit = 0
    average = 0
    increase_amount = 0
    increase_date = "Null"
    decrease_amount = 0
    decrease_date = "Null"

    #calculate main numbers


    for row in csvreader:
        #total number of months
        month = month + 1
        #net total amount of profit/losses
        net_profit = net_profit + int(row[1])
        #greatest increases in profits
        if increase_amount < int(row[1]):
            increase_amount = int(row[1])
            increase_date = str(row[0])
        #greatest decreases in profits
        if decrease_amount > int(row[1]):
            decrease_amount = int(row[1])
            decrease_date = str(row[0])
        #average of changes in profit/losses
    average = net_profit / month
    
    #print results
    
    line1 = "Financial Analysis"
    print('\033[1m' + line1)
    line2 = "----------------------------"
    print('\033[0m' + line2)
    line3 = "Total Months: " + str(month) + " months"
    print(line3)
    line4 = "Total Profit: $" + str(net_profit)
    print(line4)
    line5 = "Average Monthly Change: $" + str(int(average)) 
    print(line5)
    line6 = "Biggest Gain: " + str(increase_date) + " ($" + str(increase_amount) + ")"
    print(line6)
    line7 = "Biggest Loss: " + str(decrease_date) + " ($" + str(decrease_amount) + ")"
    print(line7)
