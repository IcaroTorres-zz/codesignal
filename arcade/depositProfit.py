
import math
# first way a normal while with incremental count
def depositProfit(deposit, rate, threshold):
    times = 0
    while deposit < threshold:
        deposit += float(deposit*rate/100)
        times += 1

    return times
print depositProfit(100,20,170)

#second way, much beautiful with math functions
##math.ceil return the lowest float above given argument
##math.log With one argument, return the natural logarithm of x (to base e).
##With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
def depositProfit2(deposit, rate, threshold):
    return math.ceil(math.log(threshold * 1.0 / deposit, 1.0 + rate / 100.0))

print depositProfit2(100,20,170)



'''
You have deposited a specific amount of dollars into your bank account. Each year your balance increases at the same growth rate. Find out how long it would take for your balance to pass a specific threshold with the assumption that you don't make any additional deposits.

Example

For deposit = 100, rate = 20 and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money on your account increases by 20%. It means that throughout the years your balance would be:

year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172,8.
Thus, it will take 3 years for your balance to pass the threshold, which is the answer.
'''
