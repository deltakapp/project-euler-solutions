# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be: 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def evenFibonacciSum(a, b, limit, evenSum = 0):
  if b > limit: # base case: if b > limit
    return evenSum
  else:
    if b %2 == 0: # if b is even, add it to the evenSum
      evenSum += b
    c = a + b
    return evenFibonacciSum(b, c, limit, evenSum)

print(evenFibonacciSum(1, 2, 4000000))