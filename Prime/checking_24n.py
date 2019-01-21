from math import sqrt
primes = [2, 3]
remainder = []
i = 5

def exit_routine():
    print(primes[-1])
    print(remainder)
    for i in range(len(remainder)-3):
        if(remainder[i] == remainder[i+1]):
            if(remainder[i+1] == remainder[i+2]):
                print(primes[i+2:i+5], "\t", remainder[i: i+3], "****")
            else:
                print(primes[i+2:i+5], "\t", remainder[i: i+3])
    exit()

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
        rem = i % 6
        remainder.append(rem)
        # if (i % 6 != 1) & (i % 6 != 5):
        # print(i, '\t', rem)
        if(len(primes) == 100):
            exit_routine()
    # print(i, len(primes))
    i+=2


