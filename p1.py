# Problem 1 - Least Factorial

def leastFactorial(n):

    # constraints applied 1<=n<=120
    if n>=1 and n<=120:
        fact = 1
        for i in range(2, n+1):
            fact = fact*i
            if fact >= n:
                return fact

    # returns -1 when exceeding constraints
    else:
        return -1


# Uncomment to print test cases
'''
leastFactorial(17)
leastFactorial(5)
leastFactorial(106)
leastFactorial(500)
leastFactorial(-10)
'''