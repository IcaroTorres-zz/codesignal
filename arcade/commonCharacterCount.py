def commonCharacterCount(s1, s2):
    o1 = char_occur(s1)
    o2 = char_occur(s2)
    result = 0
    for i in o1.keys():
      for j in o2.keys():
        if (i==j):
          result += min(o1[i],o2[i])
    return result

def char_occur(s):
  occur = {}
  for i in s:
    occur[i] = s.count(i)
  return occur


s1="aabbac"
s2="bbccaa"


print commonCharacterCount(s1,s2)
