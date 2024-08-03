# Probem Statement: Max Discounts

# A service provider is providing offers on n services, but they will use "logical OR" instead of "+" for calculating the total discount.
# There is a given array, discounts, of n integers, where discounts[i] represents the discount of the ith service. 
# The service provider has a promotion where if anyone buys ith service t times, the discount for ith service is discounts[i] x 2^(i-1). 

# Assume all the n services are bought once, and an additional k services must be purchased.
# Find the maximum achievable discount in total cost.

# Note: The service provider is using "logical OR" for calculating the total discount.


# Brute Force Approach:

def getOR(arr):
    valueOR = 0
    for i in arr:
        valueOR |= i
    return valueOR

def getMaxDiscount(discounts, k):
    n = len(discounts)
    maxDiscount = getOR(discounts)
    copyDiscounts = discounts.copy()
    
    for i in range(1, k+1):
        multiplier = 2 ** i
        for j in range(n):
            original_value = copyDiscounts[j]
            copyDiscounts[j] = discounts[j] * multiplier
            tempMaxDiscount = getOR(copyDiscounts)
            
            if tempMaxDiscount > maxDiscount:
                maxDiscount = tempMaxDiscount
            
            copyDiscounts[j] = original_value
    
    return maxDiscount

discounts = [12, 12, 9]
k = 1
print(getMaxDiscount(discounts, k))  # ExpectedOutput: 30

discounts = [10, 1]
k = 1
print(getMaxDiscount(discounts, k))  # ExpectedOutput: 21

discounts = [5, 8]
k = 3
print(getMaxDiscount(discounts, k))  # ExpectedOutput: 69


# Bitwise Contribution Counting with Temporary Bit Removal Approach
# #Bit_Manipulation #Greedy_Algorithm #Dynamic_Programming


# Code Summary:-

# Counting Bit Contributions:
# bitCount tracks how many times each bit position (from 0 to 31) is set across all discounts.

# Evaluating Each Service:
# For each service, temporarily reduce the bit counts, calculate the potential maximum discount if that service is purchased an additional number of times, and then restore the bit counts.

# Calculating Maximum Discount:
# Use the bitCount to determine the OR value of all services and compare it with the calculated discount from additional purchases to find the maximum discount possible.

def getMaxDiscount(numServices, additionalPurchases, discounts):
    # Count the occurrences of each bit position across all services
    bit_count = {}
    
    for discount in discounts:
        for bit_pos in range(32):
            bit_mask = 1 << bit_pos
            if bit_mask & discount:
                if bit_pos in bit_count:
                    bit_count[bit_pos] += 1
                else:
                    bit_count[bit_pos] = 1
    
    max_discount = float('-inf')
    
    # Evaluate the effect of additional purchases for each service
    for original_discount in discounts:
        # Temporarily reduce bit counts for the current service
        for bit_pos in range(32):
            bit_mask = 1 << bit_pos
            if bit_mask & original_discount:
                bit_count[bit_pos] -= 1
        
        # Compute the new discount value if the service is purchased additional times
        increased_discount = original_discount * (1 << additionalPurchases)
        temp_discount = 0

        # Compute the OR value based on the modified bit counts
        for bit_pos, count in bit_count.items():
            if count > 0:  # Only include bits still contributing
                temp_discount += (1 << bit_pos)

        # Include the additional purchased service's impact
        temp_discount |= increased_discount

        # Update the maximum discount found
        max_discount = max(max_discount, temp_discount)

        # Restore bit counts for the current service
        for bit_pos in range(32):
            bit_mask = 1 << bit_pos
            if bit_mask & original_discount:
                bit_count[bit_pos] += 1

    return max_discount

# Example usage:
# Example 01
numServices = 3
additionalPurchases = 1
discounts = [12, 12, 9]
print(getMaxDiscount(numServices, additionalPurchases, discounts))  # Expected output: 29

# Example 02
numServices = 2
additionalPurchases = 1
discounts = [10, 1]
print(getMaxDiscount(numServices, additionalPurchases, discounts))  # Expected output: 21

# Example 03
numServices = 2
additionalPurchases = 3
discounts = [5, 8]
print(getMaxDiscount(numServices, additionalPurchases, discounts))  # Expected output: 69
