from math import sqrt, gcd
import string

alph = string.ascii_uppercase

t = int(input())
for i in range(1,t+1):
	n,l = list(map(int,input().split()))
	num = list(map(int,input().split()))

	primes = set()
	for j in range(1,len(num)):
		g = gcd(num[j-1],num[j])
		if g != num[j]:
			primes.add(num[j-1]//g)
			primes.add(g)
			primes.add(num[j]//g)

	assert len(primes) == 26
	primes = list(primes)
	primes.sort()
	assert primes[0] >= 2

	mapping = {}
	for j in range(len(primes)):
		mapping[primes[j]]=alph[j]

	numList=[]
	for j in range(1,len(num)):
		g = gcd(num[j-1],num[j])
		if num[j-1] == num[j]:
			g = int(sqrt(num[j]))

		if len(numList) == 0:
			numList.append(num[j-1]//g)
			numList.append(g)
		
		assert numList[-2] == num[j-1]//g
		assert numList[-1] == g
		numList.append(num[j]//g)

	print('Case #'+str(i)+': ',end='')
	for ind in numList:
		print(mapping[ind],end='')
	print()