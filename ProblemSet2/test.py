d = {'C': [2, 4], 't': [], 'w': [13, 2, 4, 13, 6], 'F': [12]}

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    res = 0
    for key in aDict.keys():
        print key
        res += len(aDict[key])
    return res

print howMany(d)
