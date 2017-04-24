# Given a string, return its encoding defined as follows:
# First, the string is divided into the least possible number of disjoint
# substrings consisting of identical characters. for example, "aabbbc" is
# divided into ["aa", "bbb", "c"]. Next, each substring with length greater
# than one is replaced with a concatenation of its length and the repeating
# character. for example, substring "bbb" is replaced by "3b". Finally, all
# the new strings are concatenated together in the same order and a new string
# is returned.


# this is O == n
def lineEncoding(s):

    d ={s[0]:1}  # start a dict with the first character and its count == 1
    st='' # this will be our final string, beggining as empty word

    # from the second till the last character
    for i in range (1,len(s)):

        try: # increment if in the dict
            d[s[i]]+=1
        except: # check the last character situation in the dict
            if d[s[i-1]]==1:
                st+=s[i-1] # concatenate with our string if count is == 1
            else:
                st+=str(d[s[i-1]])+s[i-1] # concatenate count and character
            d.__delitem__(s[i-1]) # remove from dict after concatenate
            d[s[i]]=1 # start the new key with value 1 inside

        # reach the last character
        if i == len(s)-1:
            if d[s[i]]==1:
                st+=s[i] # concatenate it cause no other equals beside this last
            else:
                st+=str(d[s[i]])+s[i] # concatenate count and value together
    return st




# print lineEncoding2("abbcabb")
print lineEncoding2("aaabaaab")
