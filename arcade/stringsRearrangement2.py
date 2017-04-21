# -*- coding: utf-8 -*-
'''
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

    For inputArray = ["aba", "bbb", "bab"], the output should be
    stringsRearrangement(inputArray) = False;

    All rearrangements don't satisfy the description condition.

    For inputArray = ["ab", "bb", "aa"], the output should be
    stringsRearrangement(inputArray) = True.

    Strings can be rearranged in the following way: "aa", "ab", "bb".
'''
#maybe unnecessary
def swap(i,j,inputArray):
  print "swaped %s com %s nas posicoes %s e %s  "% (inputArray[i],inputArray[j],i,j)
  inputArray[i],inputArray[j] = inputArray[j], inputArray[i]
  return

def bruteForce(level, inputArray):
  print "iniciado o level: %s. estado do array = %s"%(level,inputArray)
  if level == len(inputArray):
    print "atingido fim desse nivel em %s == %s"% (level,len(inputArray))
    for i in range(len(inputArray)-1):
      print "verificando strings: %s e %s"%(inputArray[i],inputArray[i+1])
      dif_count = 0
      for j in range(len(inputArray[i])):
        print "verificando chars %s e %s"% (inputArray[i][j],inputArray[i+1][j])
        if inputArray[i][j]!=inputArray[i+1][j]:
          dif_count +=1
        print "diferencas encontradas= %s"%dif_count
      print "total de diferenças= %s"%dif_count
      if dif_count!=1:
        print "strings não diferem em apenas um char"
        return False
    print "strings diferem em apenas um char"
    return True

  for l in range (level,len(inputArray)):
    print "iniciando loop for l = %s no alcance entre %s até %s"% (l,level,len(inputArray))
    swap(level, l,inputArray)
    if bruteForce(level + 1, inputArray):
      print "loop seguinte verdadeiro. level == %s, com entrada final igual a %s"%(level+1,inputArray)
      return True

    swap(level, l,inputArray)
  return False


def stringsRearrangement(inputArray):
  print "rearranjando tudo! espere uns momentos..."
  return bruteForce(0,inputArray)

print stringsRearrangement(["aba",  "bbb",  "bab"])

print stringsRearrangement(["ab",  "bb",  "aa"])
print stringsRearrangement(["q",  "q"])
print stringsRearrangement(["zzzzab",  "zzzzbb",  "zzzzaa"])
print stringsRearrangement(["ab",  "ad",  "ef",  "eg"])
print stringsRearrangement(["abc",  "abx",  "axx",  "abc"])
print stringsRearrangement(["abc",  "abx",  "axx",  "abx",  "abc"])
print stringsRearrangement(["f",  "g",  "a",  "h"])
