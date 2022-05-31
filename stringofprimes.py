string = '2357111317192329'

# Initialize a list
primes = ''
possiblePrime = 2
#for possiblePrime in range(2, len(primes)>10000):
while len(primes)<10000:
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
            possiblePrime += 1
      
    if isPrime:
        primes= primes+str(possiblePrime)
        possiblePrime += 1

#print(primes)

def solution(i):
    try:
        if i >= 0 and i <= 10000:
            idnum = primes[i:i+5]
            print(str(idnum))
    except ValueError:
        print("That's not an int!")
    


solution(5000)
print(len(primes))