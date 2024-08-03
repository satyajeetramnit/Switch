# Probem Statement: Max Discounts

A service provider is providing offers on n services, but they will use "logical OR" instead of "+" for calculating the total discount.
There is a given array, discounts, of n integers, where discounts[i] represents the discount of the ith service. 
The service provider has a promotion where if anyone buys ith service t times, the discount for ith service is discounts[i] x 2^(i-1). 

Assume all the n services are bought once, and an additional k services must be purchased.
Find the maximum achievable discount in total cost.

> Note: The service provider is using "logical OR" for calculating the total discount.


Bitwise Contribution Counting with Temporary Bit Removal Approach
#Bit_Manipulation #Greedy_Algorithm #Dynamic_Programming

``` cpp
#include <bits/stdc++.h>
using namespace std;

int getMaxDiscount(int numServices, int additionalPurchases, vector<int> discounts){
    map<int, int> bitCount;
    
    // Count the occurrences of each bit position across all services
    for(auto &discount : discounts) {
        for(int bitPos = 0; bitPos < 32; bitPos++) {
            int bitMask = 1ll << bitPos;
            if(bitMask & discount) bitCount[bitPos]++;
        }
    }
    
    int maxDiscount = INT_MIN;
    
    // Evaluate the effect of additional purchases for each service
    for(auto &originalDiscount : discounts) {
        // Temporarily reduce bit counts for the current service
        for(int bitPos = 0; bitPos < 32; bitPos++) {
            int bitMask = 1ll << bitPos;
            if(bitMask & originalDiscount) bitCount[bitPos]--;
        }

        // Compute the new discount value if the service is purchased additional times
        int increasedDiscount = originalDiscount * (1ll << additionalPurchases); 
        int tempDiscount = 0;

        // Compute the OR value based on the modified bit counts
        for(auto &bit : bitCount) {
            if(bit.second > 0) {  // Only include bits still contributing
                tempDiscount += (1ll << bit.first);
            }
        }

        // Include the additional purchased service's impact
        tempDiscount |= increasedDiscount;

        // Update the maximum discount found
        maxDiscount = max(maxDiscount, tempDiscount);

        // Restore bit counts for the current service
        for(int bitPos = 0; bitPos < 32; bitPos++) {
            int bitMask = 1ll << bitPos;
            if(bitMask & originalDiscount) bitCount[bitPos]++;
        }
    }

    return maxDiscount;
}

int main() {    
    // Example 01
    int numServices = 3;  
    int additionalPurchases = 1;  
    vector<int> discounts = {12, 12, 9}; 
    cout << getMaxDiscount(numServices, additionalPurchases, discounts) << "\n";

    // Example 02
    numServices = 2;  
    additionalPurchases = 1;  
    discounts = {10, 1}; 
    cout << getMaxDiscount(numServices, additionalPurchases, discounts) << "\n";

    // Example 03
    numServices = 2;  
    additionalPurchases = 3;  
    discounts = {5, 8};  
    cout << getMaxDiscount(numServices, additionalPurchases, discounts) << "\n";

    return 0;
}
```


## Code Summary:-

Counting Bit Contributions:
bitCount tracks how many times each bit position (from 0 to 31) is set across all discounts.

Evaluating Each Service:
For each service, temporarily reduce the bit counts, calculate the potential maximum discount if that service is purchased an additional number of times, and then restore the bit counts.

Calculating Maximum Discount:
Use the bitCount to determine the OR value of all services and compare it with the calculated discount from additional purchases to find the maximum discount possible.
