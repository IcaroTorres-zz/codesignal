def longestDigitsPrefix(inputString):
    s=''
    i=0
    while inputString[i].isdigit() and i < len(inputString):
        s+=inputString[i]
        i+=1
    return s
