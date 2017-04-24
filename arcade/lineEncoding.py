# this is O == n^n in worst case
def lineEncoding(s):
    s2=''
    for ch in s:
        if ch not in s2:
            s2+= ch if s.count(ch)==1 else str(s.count(ch))+ch

    return s2

# this is O == n
def lineEncoding2(s):
    s2=''
    c=1
    for p,n in zip(s[:-1],s[1:]):
        # previous and next are equals
        if p==n:
            c+=1
            # next is last element in s
            if n==s[-1]:
                s2+=str(c)+p # concatenate s2+count of previous+previous
                c=1 # reset count
        # previous and next are differents and count of previous is 1
        elif c==1:
            s2+=p # concatenate s2+ previous
            c=1 # reset count
        # previous and next are differents and count of previous is bigger than 1
        elif c>1:
            s2+=str(c)+p # concatenate s2+count of previous+previous
            c=1 # reset count
            # then check if next is the last
            if n==s[-1]:
                s2+=n # concatenate next if it is the last

    return s2 # return the new string

print lineEncoding2("aaadddccz")
