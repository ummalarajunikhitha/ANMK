public class prime{

    public static void main(String[] args) {
        System.out.println("Prime numbers between 1 and 500 are:");
        for (int i = 2; i <= 500; i++) { // Start from 2 as 1 is not prime
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }

    // Helper method to check if a number is prime
    public static boolean isPrime(int number) {
        if (number <= 1) { // 0 and 1 are not prime numbers
            return false;
        }
        // Check for divisibility from 2 up to the square root of the number
        // This optimizes the check as any factor greater than the square root
        // would have a corresponding factor smaller than the square root.
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // If divisible, it's not prime
            }
        }
        return true; // If no divisors found, it's prime
    }

}


