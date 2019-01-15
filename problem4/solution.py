'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
for i in range(997, 100, -1):
    Str = str(i)
    num = int(Str + Str[::-1])
    for j in range(999, 100, -1):
        if(num % j == 0):
            if (1000 > num / j > 99):
                print (j, " * ", num/j, " = ", num)
                exit()
