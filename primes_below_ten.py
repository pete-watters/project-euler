n = 10 
i = 1

while i <= n:
	i += 1
	j = 1
	while j <= n:
		if i % j:
			print(i)
			j += 1
		else:
			j += 1

"""
def primes(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            print(i)
            n //= i
    return n

print(primes(n))
"""
