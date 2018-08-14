n=5000 
while True:
	n = 0
	for i in range(2,10):
		n +=1
		if n % i == 0:
			i += 1
			print(i)
