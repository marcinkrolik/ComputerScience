def genPrimes():
    
    primes = [2]
    candidate = primes[-1]
    while True:
        flag = True
        candidate += 1
        for prime in primes:
            if (candidate % prime) == 0:
                flag = False
        if flag == True:
            yield primes[-1]
            primes.append(candidate)
            
g = genPrimes()
'''while True:
    print g.next()
    aa = raw_input()
'''
import string
print string.punctuation
tt = "a'b"
for c in tt:
    print c in string.punctuation 
            
    