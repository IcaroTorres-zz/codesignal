def digitDegree(n):
    i=0
    return degreetor(n,i)

def degreetor(n,i):
    s=0
    if n>9:
        for num in list(str(n)):
            s+=int(num)
        i+=1
        return degreetor(s,i)
    else:
        return i

print digitDegree(195864)
print digitDegree(195864195864195864195864195864195864195864195864195864)
