import string
def isMAC48Address(inputString):
    # a list with all possible charactes
    hexx = string.digits + string.ascii_uppercase[:6]
    s=inputString.split('-')
    # check if s has 6 positions, each one with 2 chars, and each char in hexx
    if len(s) == 6 and (all(len(i)==2 and i[0] in hexx and i[1] in hexx for i in s) ):
        return True
    else:
        return False


print isMAC48Address("A0-A2-A2-A4-B2-C8")
