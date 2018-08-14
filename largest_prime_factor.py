"https://stackoverflow.com/a/22808285/1365580"

n = 600851475143 

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
            print(n%i)
        else:
            n //= i
    return n

print(largest_prime_factor(n))

