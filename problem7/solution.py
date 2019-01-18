

from math import sqrt
primes = [2]
i = 3
while(True):
    prime_flag = True
    srt = sqrt(i)
    for p in primes:
        if p > srt:
            break
        if i % p == 0:
            prime_flag = False
            break
    if(prime_flag):
        primes.append(i)
        if(len(primes) == 10001):
            print(primes[-1])
            exit()
    # print(i, len(primes))
    i+=2
