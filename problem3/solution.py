'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

num = 600851475143 
while num % 2 == 0:
    num /= 2
i = 3
while num != i:
    while num % i == 0:
        num /= i
        print(str(num) + ", " + str(i))
    i += 2
print(i)
