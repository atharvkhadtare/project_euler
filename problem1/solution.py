'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
def ap(num):
	return (num * (num + 1)/2)
def solution(limit, num1, num2):
	limit -= 1
	SUM = num1 * ap(int(limit/num1))
	SUM += num2 * ap(int(limit/num2))
	num1 *= num2
	SUM -= num1 * ap(int(limit/num1))
	return SUM
print(solution(1000, 3, 5))
