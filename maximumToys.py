def maximumToys(prices, k):
"""
return an integer representing the maximum number of toys Mark can purchase

parameters:
prices: an array of integers representing toy prices
k: an integer, Mark's budget
"""
    ordered_prices = sorted(prices)
    n_toys = 0
    total = 0

    for _, price in enumerate(ordered_prices):
        if total < k and total + price <= k:
            total += price
            n_toys+=1
        else:
            return n_toys