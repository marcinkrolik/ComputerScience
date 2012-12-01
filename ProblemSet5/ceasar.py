import string

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
    left = string.punctuation + ' 0123456789' 
    
    for char in text:
        
        if char in left:
            encrypted += char
        else:
            encrypted += coder[char]
    
    return encrypted

def applyShift(text, shift):
    
    return applyCoder(text, buildCoder(shift))


print applyShift("Hello", 3)
print applyShift("Fg, tml lzwjw ak s LS fsewv SdnAf!", 8)    
    


    