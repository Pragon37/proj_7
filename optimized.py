"""The program read one of 3 dataset and then computes the optimal selection of shares
that will provide the return on investment. It uses the so-called knapsack algorithm to
compute this optimal invetsment"""

import time
import itertools
import csv

"""Select one of the 3 csv dataset"""
testSet = input("Type test number 0,1,2  default 0 :")

if testSet == '1':
    dataSet = 'CSV/dataset1_Python+P7.csv'
    MAXINVESTEMENT = 50000
    scale = 100
elif testSet == '2':
    dataSet = 'CSV/dataset2_Python+P7.csv'
    MAXINVESTEMENT = 50000
    scale = 100
else:
    dataSet = 'CSV/dataset0_Python+P7.csv'
    MAXINVESTEMENT = 500
    scale = 1


shares = []

"""Read the selected csv dataset, filter out unconsistent data (negative or null values)
and create a structure to hold the data"""
with open(dataSet, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if not (row[0] == 'name' or float(row[1]) <= 0 or float(row[2]) <= 0):
            shares.append([row[0], int(scale*float(row[1])), int(scale*float(row[2]))])

print("Number of shares:", len(shares))

earnings = []
profits = []

for share in shares:
    earnings.append([share[1], share[1] * share[2]])

start_time = time.time()
profit = []

"""Initialize the data structure that holds the intermediate solutions"""
profit = [list(itertools.repeat(0, MAXINVESTEMENT+1)) for _ in range(0, len(shares) + 1)]

"""Iterate the computation of the profit for each share addition,
for all possible values less than the maximum allowed"""
for ShareNum, share in enumerate(earnings):
    ShareNum += 1
    for curInvest in range(1, MAXINVESTEMENT + 1):
        if share[0] <= curInvest:
            profit[ShareNum][curInvest] = max(share[1] + profit[ShareNum-1][curInvest - share[0]], profit[ShareNum-1][curInvest])
        else:
            profit[ShareNum][curInvest] = profit[ShareNum-1][curInvest]


bestProfit = profit[-1][-1]

currentProfit = bestProfit
currentInvestment = MAXINVESTEMENT
shareSelection = []

"""Find the share selection that provide the maximum profit"""
for share in range(len(shares), 0, -1):
    if profit[share][currentInvestment] == profit[share-1][currentInvestment]:
        """0 when share is not selected"""
        shareSelection.append([share, currentInvestment, 0, shares[share-1][1], currentInvestment, currentProfit])
    else:
        """1 when share is selected"""
        for investment in range(currentInvestment, 0, -1):
            if not (profit[share][investment] >= currentProfit):
                shareSelection.append([share, investment + 1, 1, shares[share-1][1], currentInvestment, currentProfit])
                currentInvestment = investment + 1 - shares[share-1][1]
                currentProfit = profit[share-1][currentInvestment]
                break

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time :", elapsed_time)

profit = 0
investment = 0

"""Format and report the results"""
print("\n")
for share in shareSelection:
    if share[2]:
        print('{0:<10s}{1:<7s}{2:<6.2f}{3:<7s}{4:<10.6f}'.
              format(shares[share[0]-1][0], "  Value:", shares[share[0]-1][1] / scale,
                     "  Profit:", shares[share[0]-1][1] * shares[share[0]-1][2] / (100 * scale * scale)))
        investment += shares[share[0]-1][1]
        profit = profit + (shares[share[0]-1][1] * shares[share[0]-1][2])
print("\n")

print("Total investment:", investment / scale)
print("Total profit:", profit / (100 * scale * scale))
