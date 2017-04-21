def allLongestStrings(inputArray):
        d = {}
        higestSize = 0;
        for word in inputArray:
                try:
                        updated = d[len(str(word))]
                except:
                        updated = []
                updated.append(str(word))
                d[len(str(word))] = updated
                if higestSize < len(str(word)):
                        higestSize = len(str(word))
        return d[higestSize]
