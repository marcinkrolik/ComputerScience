# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if len(aStr) == 1:
        return aStr
    else:
        newString = reverseString(aStr[1:]) + aStr[0]
        return newString

print reverseString('abcde')    
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    
    two base cases: if length of x is zero return True

    if length of x is greater than zero and the first character of x is not in word (at any location) return False

    recursive case: determine the index of the first occurrence of first character in x in word

    recurse into function using first letter in x as x and word sliced to remove everything before said index as word.
    """
    ###TODO.
    if len(x) == 0: 
        return True
    
    elif x[0] not in word:
        return False
    
    else:
        index = word.index(x[0])
        newX = x[1:]
        newWord = word[index:] 
        return x_ian(newX, newWord)


print x_ian('alvin', 'palavering')
#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text)<lineLength:
        return text
 
    break_point = text.find(' ', lineLength-1)
    if break_point == -1:
        return text
   
    return text[0:break_point] + '\n' + insertNewlines(text[break_point+1:], lineLength)

t = "While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together."
print insertNewlines(t, 15)
