def isIPv4Address(inputString):
    sl = inputString.split('.')
    if len(sl)== 4 and all(s.isdigit() for s in sl):
        for n in sl:
            number = int(n)
            if number <-1 or number > 255:
                return False
        return True
    else:
        return False
