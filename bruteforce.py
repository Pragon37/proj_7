"""The program read the dataset below and computes the profit for all possible set of shares"""

import time
import itertools

shares = [['Action_1', 20, 5],
          ['Action_2', 30, 10],
          ['Action_3', 50, 15],
          ['Action_4', 70, 20],
          ['Action_5', 60, 17],
          ['Action_6', 80, 25],
          ['Action_7', 22, 7],
          ['Action_8', 26, 11],
          ['Action_9', 48, 13],
          ['Action_10', 34, 27],
          ['Action_11', 42, 17],
          ['Action_12', 110,  9],
          ['Action_13', 38, 23],
          ['Action_14', 14, 1],
          ['Action_15', 18, 3],
          ['Action_16', 8, 8],
          ['Action_17', 4, 12],
          ['Action_18', 10, 14],
          ['Action_19', 24, 21],
          ['Action_20', 114, 18]]

shares_values = [share[1] for share in shares]

MAXINVESTMENT = 500
SHARENUM = len(shares)
print("Number of shares:", SHARENUM)
earnings = []

for share in shares:
    earnings.append(share[1] * share[2])

start_time = time.time()
bestProfit = 0
"""For a set of N shares there are 2**N  possible different subsets"""
"""use itertools compress to select the subset elements and sum for a faster addition of share benefit"""
"""the selection mask (binary value) needs to have SHARENUM bits to get a correct result."""
for i in range(0, 2**SHARENUM):
    profit = sum(itertools.compress(earnings, map(int, bin(i)[2:][:].zfill(SHARENUM))))
    if profit >= bestProfit:
        investment = sum(itertools.compress(shares_values, map(int, bin(i)[2:][:].zfill(SHARENUM))))
        if investment <= MAXINVESTMENT:
            bestProfit = profit
            bestCandidate = bin(i)[2:][:].zfill(SHARENUM)
            bestRank = i
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time iterating the main loop:", elapsed_time)


"""Format and print results"""

print("Investment:", sum(itertools.compress(shares_values, map(int, bin(bestRank)[2:][:].zfill(SHARENUM)))))
print("Max profit:", bestProfit / 100)

print("\n")
for share in (list(itertools.compress(shares, map(int, bin(bestRank)[2:][:].zfill(SHARENUM))))):
    print('{0:<10s}{1:<7s}{2:<6.2f}{3:<7s}{4:<10.6f}'.
          format(share[0], "  Value:", share[1], "  Profit:", share[1] * share[2]))
