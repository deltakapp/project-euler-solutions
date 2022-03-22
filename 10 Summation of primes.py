# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
from math import sqrt


def sumPrimeFactors(target):
  firstPrime = [2]
  primes = [3] # holds primes (2 is omitted for efficiency and inserted later)
  candidate = 5 # first candidate for a prime

  def check(candidate): # check if candidate is prime
    cap = int(sqrt(candidate))

    for x in primes: #check the list of primes for factors of candidate
      if candidate % x == 0: # if candidate has a prime factor, it isn't prime
        return

      # if no prime factor <= sqrt(candidate) then candidate is prime
      if x > cap:
        primes.append(candidate)
        return
  
  while candidate < target:
    check(candidate)
    candidate += 2 # increment to next odd candidate
  
  primes = firstPrime + primes # add [2] to start of primes list

  return sum(primes)

print(sumPrimeFactors(2000000))
