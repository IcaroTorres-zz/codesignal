import binascii
def messageFromBinaryCode(code):
    print binascii.unhexlify('%x' % int(code, 2))

def messageFromBinaryCode3(code):
    return "".join([chr(int(code[8*i:8*i+8],2)) for i in range(len(code)//8)])

print messageFromBinaryCode3("010010000110010101101100011011000110111100100001")
