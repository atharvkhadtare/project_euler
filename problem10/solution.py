from math import sqrt
primes = [2, 3, 5]
exceptions = []
rem = []
i = 5
# total_sum = 6 * 33333 * 33334 - 5
total_sum = 10
while i < 199998:
# while i < 104742:
    i += 2
    srt = sqrt(i)
    for p in primes:
        if p > srt:
            total_sum += i
            primes.append(i)
            break
        if i % p == 0:
            break
    if i > 199995:
    # if i > 104739:
        break
    i += 4
    srt = sqrt(i)
    for p in primes:
        if p > srt:
            total_sum += i
            primes.append(i)
            break
        if i % p == 0:
            break
print (primes)
# print(exceptions)
print(len(primes))
print(total_sum)
