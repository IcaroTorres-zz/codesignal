# given a string, return a new string with each characters shifted to the next in alphabet
import string
def alphabeticShift(inputString):

    s = list(inputString) #cast to list
    l = list(string.letters) # string.lettes == alphabetic lower and upper cases

    #slicing list l creating lowercase and uppercase lists "s_a" and "s_A"
    s_a, s_A = l[:len(l)/2]+['a'], l[len(l)/2:]+['A']

    #dict comprehension
    dic_s_a = {p:f for p,f in zip(s_a[:-1],s_a[1:])}
    dic_s_A = {p:f for p,f in zip(s_A[:-1],s_A[1:])}
    #dic with both previous togheter
    dic = dict(dic_s_a.items()+dic_s_A.items())

    #changing chars in the list "s" cause values in string index <inputString[index]>
    #can't be assigned
    for i,ch in enumerate(s):
      s[i] = dic[ch]

    #join empty char with all list s making a string
    return ''.join(s)

print alphabeticShift("crazy")
