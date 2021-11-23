import time, itertools

SHARES = [[20 , 5],
[30 , 10],
[50 , 15],
[70 , 20],
[60 , 17],
[80 , 25],
[22 , 7],
[26 , 11],
[48 , 13],
[34 , 27],
[42 , 17],
[110 ,  9],
[38 , 23],
[14 , 1],
[18 , 3],
[8 , 8],
[4 , 12],
[10 , 14],
[24  , 21],
[114 , 18]]           

SHARES_VALUES = [share[0] for share in SHARES]
SORTED_SHARES_VALUES = sorted(SHARES_VALUES)
print(SHARES_VALUES)



SORTED_SHARES_BENEFIT = sorted(SHARES, key=lambda field: field[1])

EARNINGS = []
profits = []

for SHARE in SHARES:
     EARNINGS.append(SHARE[0] * SHARE[1])

start_time = time.time()
bestProfit = 0
for i in range(0, 2**20):
    profit = sum(itertools.compress(EARNINGS, map(int,bin(i)[2:][:].zfill(20))))
    if profit >= bestProfit:
        investment = sum(itertools.compress(SHARES_VALUES, map(int,bin(i)[2:][:].zfill(20))))
        if investment <= 500:
#            print(investment,bestProfit,profit)
            bestProfit = profit
            bestCandidate= bin(i)[2:][:].zfill(20)
            bestRank = i
            profits.append(profit)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time iterating the main loop:", elapsed_time)

print("Max profit:", bestProfit)
print("Rank=", bestRank,"Selection:",bestCandidate)
print(list(itertools.compress(SHARES_VALUES, map(int,bin(bestRank)[2:][:].zfill(20)))))
print("Investment:",sum(itertools.compress(SHARES_VALUES, map(int,bin(bestRank)[2:][:].zfill(20)))))
print(list(itertools.compress(SHARES, map(int,bin(bestRank)[2:][:].zfill(20)))))


"""
print("Profit table Length: ",len(profits))
sweetSpot = max(profits)
print(sweetSpot)
print(profits.index(sweetSpot))

profit = 0
investment = 0
print("The winning selection:\n")
for j,digit in enumerate(bin(640663)[2:][:]):
    profit += int(digit) * EARNINGS[j]
    investment += int(digit) * SHARES[j][0]
    if digit == '1':
        print("Share: ",j," \n")
        print(investment)
print("PROFIT = ", profit)
print("INVESTMENT = ", investment)

"""
