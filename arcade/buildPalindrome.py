def palindrome(s):
    return s==s[::-1]

def buildPalindrome2(s):
    d={}
    if palindrome(s):
        d[len(s)]=s
    else:
        for i in range (1,len(s)+1):
            for j in range (1,len(s)+1):
                tmp = (s + s[-j:-i][::-1])
                if palindrome(tmp):
                    d[len(tmp)]=tmp

    return sorted(d.items())[0][1]


print buildPalindrome2 ("abcdefgff")
print buildPalindrome2 ("arara")
print buildPalindrome2 ("aarg")
print buildPalindrome2 ("gdftraaa")
print buildPalindrome2 ("fd")
print buildPalindrome2 ("banana")
