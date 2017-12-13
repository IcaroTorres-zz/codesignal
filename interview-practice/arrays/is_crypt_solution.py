'''Codefights intreview practice - Arrays - "isCryptSolution"'''
# Disclaimer
'''A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence
between letters and digits, such that the given arithmetic equation consisting of letters
holds true when the letters are converted to digits.'''
def isCryptSolution(crypt, solution):
    '''isCryptSolution([str1, str2, str3], [[a1, b1], [a2, b2]...]) -> boolean\n
    You have an array of strings crypt, the cryptarithm, and an an array containing the
    mapping of letters and digits, solution. The array crypt will contain three non-empty
    strings that follow the structure: [word1, word2, word3], which should be interpreted
    as the word1 + word2 = word3 cryptarithm.\n
    If crypt, when it is decoded by replacing all of the letters in the cryptarithm with
    digits using the mapping in solution, becomes a valid arithmetic equation containing
    no numbers with leading zeroes, the answer is true. If it does not become a valid
    arithmetic solution, the answer is false.'''
    table = {ord(k): v for k, v in solution}
    *values, = map(lambda x: x.translate(table), crypt)
    if any(_str != "0" and _str.startswith("0") for _str in values):
        return False
    else:
        return int(values[0]) + int(values[1]) == int(values[2])

CRYPT1 = ["SEND", "MORE", "MONEY"]
SOLUTION1 = [['O', '0'],
             ['M', '1'],
             ['Y', '2'],
             ['E', '5'],
             ['N', '6'],
             ['D', '7'],
             ['R', '8'],
             ['S', '9']]
CRYPT2 = ["TEN", "TWO", "ONE"]
SOLUTION2 = [['O', '1'],
             ['T', '0'],
             ['W', '9'],
             ['E', '5'],
             ['N', '4']]
print(isCryptSolution(CRYPT1, SOLUTION1))
print(isCryptSolution(CRYPT2, SOLUTION2))
