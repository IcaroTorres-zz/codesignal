'''Codefights interview practice - Hash Tables - "possibleSums"'''
def possibleSums(coins, quantity):
    '''possibleSims(list, list) -> int\n
    You have a collection of coins, and you know the values of the coins and the quantity
    of each type of coin in it. You want to know how many distinct sums you can make
    from non-empty groupings of these coins.'''
    _set = set()
    _set.add(0)
    for i, _qtd in enumerate(quantity):
        for _sum in list(_set):
            for j in range(1, _qtd + 1):
                _set.add(_sum + j * coins[i])
                print("%d + %d = %d" % (_sum, j * coins[i], _sum + j * coins[i]))

    return len(_set) - 1

COINS = [10, 50, 100]
QUANTITY = [1, 2, 1]
print(possibleSums(COINS, QUANTITY))
