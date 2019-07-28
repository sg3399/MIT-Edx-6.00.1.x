#Generate Primes

def genPrimes():
    prime_numbers=[]
    x=2
    while True:
        remainders=[x%p for p in prime_numbers]
        if 0 in remainders:
            x=x+1
        else:
            prime_numbers.append(x)
            yield x
            x=x+1

prime = genPrimes()
prime.__next__()
prime.__next__()