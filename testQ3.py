import random, string, sys, logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(message)s')

def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

primeSet = primes(10**7)
t = 1000
print(t)

for i in range(t):
	ourPrimes = random.sample(primeSet,26)
	ourPrimes.sort()

	st = string.ascii_uppercase
	X = random.randint(0,101-26)
	st = st + ''.join(random.choices(string.ascii_uppercase, k=X))
	st = ''.join(random.sample(st,len(st)))

	logging.debug(st)

	print(10000, len(st)-1)
	for j in range(len(st)-1):
		print(ourPrimes[ord(st[j])-ord('A')]*ourPrimes[ord(st[j+1])-ord('A')],end=' ')
	print()