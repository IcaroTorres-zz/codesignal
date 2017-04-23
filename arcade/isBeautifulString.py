import string
def isBeautifulString(inputString):
    l= string.ascii_lowercase[::-1]
    d={a :0 for a in l}
    for i in inputString:
        d[i]+=1
    return False if any( [ d[a]>d[b] for a,b in zip(l[:-1],l[1:]) ] ) else True

def isBeautifulString2(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]

    return r[::-1] == sorted(r)

print isBeautifulString("bbbaacdafe")
