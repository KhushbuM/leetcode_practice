#prices = [7,2,5,3,6,1]
# Output: 5

def max_profit(prices: list) -> int:
    l = 0
    r = 1
    maxProfit = 0


    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r

        r += 1

    return maxProfit            
            

prices = [1]
result = max_profit(prices)
print("Result : ", result)              
        
# cases
# [7,6,5,4,3,1]
# []
# [1]
# [1,2]