'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
factors = {}

for i in range(2, 20):
    print(i, end = " ")
    for j in range(2, i):
        f = 2   
        while(i != 1):
            count = 0
            if(i % f == 0):
                while(i % f == 0):
                    i /= f
                    count += 1
                factors[f] = max(count, factors.get(f, 0)) 
            f+=1
    print (i, " - ", factors)

product = 1
for i in factors:
    product *= i ** factors.get(i)
    print(factors.get(i), " ", product)
# num = 600851475143 
# i = 2
# while(num % i == 0):
	# num /= i
# i += 1
# while(num != 1):
	# while(num % i == 0):
		# num /= i
   #             print ( str(num) + ", " + str(i))
	# i += 2
# print (i-2)
