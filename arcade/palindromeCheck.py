#the worst way
def palindromeRearranging(inputString):
    if len(inputString)%2 ==0:
        for ch in inputString:
            if inputString.count(ch)%2 !=0:
                return False
            else:
                return True
    else:
        odd_count = 0
        for ch in inputString:
            if inputString.count(ch)%2 !=0:
                odd_count += 1
        if odd_count == 1:
            return True
        else:
            return False

#the beautiful way


print palindromeRearranging("asdsa")
print palindromeRearranging("asdsadsdsd") aa ssss dddd
print palindromeRearranging("asdsaaaaassssdd")
print palindromeRearranging("asdsaasdsa")
print palindromeRearranging("asdsasdsa")
