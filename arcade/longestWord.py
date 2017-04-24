import string
def longestWord(text):
    d={} # dict to direct acess
    w='' # new empty string to represent our new word

    for ch in text:
        # componding the new string while discovering each letter
        if ch in string.letters:
            w+=ch #concatenate to what we already have
            if ch==text[-1]: # concatenate the last word found if reachs the end
                d[len(w)]=w # put into the dict to acess directly later
                w='' # reset the temporary string to the first state
        else: # when we stop to get letters
            d[len(w)]=w # put into the dict to acess directly later
            w='' # reset the temporary string to the first state

    return d[max(d.keys())] # return the string inside the bigest key on dict
    
print longestWord("@#!!Ready, steady, go!")
print longestWord("ABCd")
