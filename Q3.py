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

	numList = [-1]*(l+1)
	j = 0
	while num[j]==num[j+1]:
		j+=1
		# numList.append(-1)
	g = gcd(num[j],num[j+1])

	numList[j] = num[j]//g
	numList[j+1] = g

	#Back-tracking, to fill in the positions
	# that we did not know earlier
	tem = j-1
	while tem >= 0:
		numList[tem] = num[tem] // numList[tem+1]
		tem -= 1

	j += 1
	# Moving on
	while j < l:
		numList[j+1] = num[j] // numList[j]
		j += 1

	# print('Case #'+str(i)+': ',end='')
	for ind in numList:
		print(mapping[ind],end='')
	print()