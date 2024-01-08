def maxProfit(prices):
    maxdiff=0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if j>i:
                diff=prices[j]-prices[i]
                if maxdiff<diff:
                    maxdiff=diff
                    print(maxdiff)
                    print([j+1,i])
    return maxdiff

print(maxProfit([7,6,4,3,1]))
