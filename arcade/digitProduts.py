import math
def digitsProduct(product):
    if product == 1:
        return 1
    elif product == 0:
        return 10
    elif all([True if ch in ["0","1"] else False for ch in str(product)]):
        t=[]
        for i in range(2,10)[::-1]:
            while product%i==0:
                product/=i
                t.append(i)
        return int( sum([t[j] * math.pow(10,j)for j in range(len(t))[::-1]]) )
    else:
        factors=[]
        for i in range(2,10)[::-1]:
            while product%i==0:
                product/=i
                factors.append(i)
        if product > 1:
            return -1
        return int( sum([factors[j] * math.pow(10,j)for j in range(len(factors))[::-1]]) )

print digitsProduct(12)
print digitsProduct(450)
print digitsProduct(1)
print digitsProduct(0)
print digitsProduct(100)
print digitsProduct(10)
print digitsProduct(17)
print digitsProduct(177)
print digitsProduct(19)
print digitsProduct(81)
print digitsProduct(599)
print digitsProduct(13)
print digitsProduct(112)
print digitsProduct(7)
print digitsProduct(20)
print digitsProduct(600)
print digitsProduct(10)
print digitsProduct(33)
