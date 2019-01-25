class Solution{

	static int ap(int num){
		return(num * (num + 1)/2);
	}

	static long	sum_of_primes(long limit, long num1, long num2){
		limit -= 1;
		long Sum = num1 * ap((int)(limit/num1));
		Sum += num2 * ap((int)(limit/num2));
		num1 *= num2;
		Sum -= num1 * ap((int)(limit/num1));
		return Sum;
	}

    public static void main(String args[]){
        System.out.println(sum_of_primes(1000, 3, 5));
    }
}   
