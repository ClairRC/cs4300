def main():
    # Check if number is positive
    is_pos_var = input("Enter a number and through the power of science and magic you will be told if it is negative, positive, or neither: ")
    is_pos_out = isPositive(float(is_pos_var))

    if is_pos_out == -1:
        print("Your number is negative!\n")
    elif is_pos_out == 0:
        print("Your number is 0!\n")
    else:
        print("Your number is positive!\n")

    # Print first 10 primes
    print("First 10 primes: " + str(findFirstNPrimes(10)))

    # Print sum of first 100 natural numbers
    print("Sum of 1-100: " + str(sumOfFirstNNumbers(100)))

# Returns 1 for positive, -1 for negative, and 0 for 0
def isPositive(a):
    if a == 0:
        return 0

    elif a < 0:
        return -1
    
    else:
        return 1

# Calcuate first n prime numbers
def findFirstNPrimes(n):
    primes = []
    num = 2 # First prime

    # The instruction SAYS to do a for loop, and like.. i DID use a for loop so
    while len(primes) < n:
        isPrime = True
        # For every number between 2 and number we're checking, check between 2 and sqrt(num) to see if its prime
        for i in range(2, int(num ** 0.5) + 1):
            # If number we're checking is divisible, it is not prime
            if num % i == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(num)

        num = num + 1

    return primes

# Calculate sum of first n natural numbers
def sumOfFirstNNumbers(n):
    if n <= 0:
        return 0

    sum = 0

    # O(n) algorithm for a task that freaking Guass did in O(1) time nerd emoji
    for i in range(n+1):
        sum += i

    return sum

    

if __name__ == "__main__":
    main()