import string

WORDLIST_FILENAME = "words.txt"
def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def buildCoder(shift):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    length = len(lower)
    map_ = {}
    
    for char in lower:
        index = lower.index(char)
        map_[char] = lower[(index+shift) % length]
    
    for char in upper:
        index = upper.index(char)
        map_[char] = upper[(index+shift) % length]
    
    return map_

def applyCoder(text, coder):
    
    encrypted = ''
    left = string.punctuation + ' 0123456789'+str('\n') 
    
    for char in text:
        
        if char in left:
            encrypted += char
        else:
            encrypted += coder[char]
    
    return encrypted

def applyShift(text, shift):
    
    return applyCoder(text, buildCoder(shift))

def findBestShift(wordList, text):
    '''
    1. Set the maximum number of real words found to 0.
    2. Set the best shift to 0.
    3. For each possible shift from 0 to 26:
    4. Shift the entire text by this shift.
    5. Split the text up into a list of the individual words.
    6. Count the number of valid words in this list.
    7. If this number of valid words is more than the largest number of
       real words found, then:
        8. Record the number of valid words.
        9. Set the best shift to the current shift.
    10. Increment the current possible shift by 1. Repeat the loop
       starting at line 3.
    11. Return the best shift.
    '''
    maxWordsFound = 0
    bestShift = 0
    for shift in range(0,26):
        wordsFound = 0
        words = applyShift(text, (26-shift)%26).split(' ')
        
        for word in words:
            if isWord(wordList, word):
                wordsFound += 1
        
        if wordsFound > maxWordsFound:
            maxWordsFound = wordsFound
            bestShift = 26-shift
    
    return bestShift
        
    
s = "Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu."
l = loadWords()
print findBestShift(l, s)

def decryptStory():
    
    l = loadWords()
    story = getStoryString().replace('\n','')
    shift = findBestShift(l, story)
    print applyShift(story, shift)
    '''
    Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.
    '''
decryptStory()


