'''
1. Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator. Comparati diferenta de timp necesara generarii.
'''
import math
import time

def is_prime(nr):
    if nr < 2 :
        return False
    for i in range(2,int(math.sqrt(nr))+1):
        if nr%i==0:
            return False
    return True

start_time = time.time()
prime_numbers = []
nr = 2
while len(prime_numbers) < 100:
    if is_prime(nr):
        prime_numbers.append(nr)
    nr += 1
end_time = time.time()

print(prime_numbers)
print(end_time-start_time,' secunde')


def gen_primes():
    nr = 2
    count = 0
    while count < 100:
        if is_prime(nr):
            yield nr
            count += 1
        nr += 1

start_time = time.time()
for elem in gen_primes():
    print(elem)
end_time = time.time()

print(end_time-start_time,' secunde')
