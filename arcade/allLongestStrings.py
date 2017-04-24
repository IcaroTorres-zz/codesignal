# return all strings in a array/list with same biggest size
def allLongestStrings(inputArray):
        d = {} # prefered dict to direct acess
        highest = 0;
        for word in inputArray:
                try: # try to get the list if it already exists
                        updated = d[len(word)]
                except: # else create a new empty list
                        updated = []

                # apend word and add this list to dict
                updated.append(word)
                d[len(word)] = updated
                # if a bigger word was found, use it to do direct acess later
                if highest < len(word):
                        highest = len(word)
        # returning directly by highest key
        return d[highest]
