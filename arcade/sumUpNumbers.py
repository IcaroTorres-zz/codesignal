import string
def sumUpNumbers(s):
    numb=''
    c=0
    for ch in s:
        if ch.isdigit(): # check if string makes a number
            numb+=ch # keep this part of number together if previous ones
            if ch == s[-1]:
                c+=int(numb) # when reach the end increase with the last number
        elif numb!='':
            c+= int(numb) # the sum is increased with our current number found
            numb ='0'
        else:
            numb='0' # if no one digit was found, keep a string with value 0
    return c

    # return sum([int(n) for n in s.split(' ') if n.isdigit()])
print sumUpNumbers("2 apples, 12 oranges")
print sumUpNumbers("123450")
print sumUpNumbers("Your payment method is invalid")
