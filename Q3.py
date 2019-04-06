from math import sqrt, gcd
import string

alph = string.ascii_uppercase
debug = True

t = int(input())
for i in range(1,t+1):
	if debug: 
		print(str(i)+" iteration")
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
	if(debug):
		print('mapping:',mapping)

	numList=[]
	for j in range(1,len(num)):
		g = gcd(num[j-1],num[j])
		if num[j-1] == num[j]:
			g = int(sqrt(num[j]))

		if len(numList) == 0:
			numList.append(num[j-1]//g)
			numList.append(g)
		
		if debug:		
			for x in numList:
				print(mapping[x],end='')
			print()
			if not numList[-2] == num[j-1]//g:
				print('num[j-1]:',num[j-1],'\tnum[j]',num[j])
				print('g:',g)
				print('numList[-2]:',numList[-2],mapping[numList[-2]])
				print('num[j-1]//g:',num[j-1]//g)
				print('num[j-1]:',num[j-1],mapping[num[j-1]])
		assert numList[-2] == num[j-1]//g
		assert numList[-1] == g
		numList.append(num[j]//g)

	print('Case #'+str(i)+': ',end='')
	for ind in numList:
		print(mapping[ind],end='')
	print()