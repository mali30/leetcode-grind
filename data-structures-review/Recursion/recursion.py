def findFactorial(n):
    # edge case
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    value = 0
    # base case 
    if n == 0 or n == 1:
        return 1
    else:
        # recursive call 
        value = n * findFactorial(n - 1)
        print('n', n )
    return value 

print(findFactorial(4))


# fibonacci numbers
# 0 1 1 2 3 5 8 13 21 34 55 ...

def findFibonacci(n):
    # edge cases
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    # base case
    if n == 1 or n == 0:
        return n
    else:
        return findFibonacci(n - 1) + findFibonacci(n - 2)
    
print(findFibonacci(5))


# find the sum of digits of a positive integer
# recursive case - 
def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer only"
    if n == 0:
        return 0
    else:
        value = int(n % 10) + sumOfDigits(n // 10)
        sumOfDig = sumOfDigits(n // 10)
        # print('value', value)
        print('sum', sumOfDig )
        return value 

print(sumOfDigits(50))

# calculate power of number using recursion
# power(2, 5) = 2 * power(2, 4)
#             = 2 * (2 * power(2, 3))
#             = 2 * (2 * (2 * power(2, 2)))
#             = 2 * (2 * (2 * (2 * power(2, 1))))
def calculatePower(base, exponent):
    
    if base == 0 or exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base +  calculatePower(base, exponent - 1)

print('power', calculatePower(5 , 5))


# Euclidean Algorithm
# gcd(a,0) = a
# gcd(a,b) = gcd(b, a mod b)
def greatestCommonDivisor(x, y):
    if x < 0:
        x = -1 * x
    if y < 0:
        y = -1 * y
    if x == 1 or y == 1:
        return x, y
    if y == 0:
        return x
    else:
        return greatestCommonDivisor(y, x%y)


print(greatestCommonDivisor(-5, 20))


def gcf(x, y):
    if x is None or y is None:
        return x, y
    if y == 0:
        return x
    else:
        return gcf(y , x % y)


# calculate power of number using recursion

def calcPower(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base + calcPower(base, base * exponent - 1)
        

# decimal to binary
# divide by 2
# get the integer quotient for next iteration 
# get remainder for the binary digit 

def decToBinary(x):
    assert x == int(x)
    if x == 0:
        return 0
    else:
        return x % 2 + 10 * decToBinary(x // 2)

print(decToBinary(5))