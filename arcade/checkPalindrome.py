def checkPalindrome(inputString):
    return (str(inputString) == str(inputString)[::-1])
'''
#JS
function checkPalindrome(inputString) {
    return inputString == inputString.split('').reverse().join('');
}

#CS
bool checkPalindrome(String inputString) {
    return inputString.SequenceEqual(inputString.Reverse());
}

#JAVA
boolean checkPalindrome(String inputString) {
    return inputString.equals(new StringBuilder(inputString).
                              reverse().toString());
}
