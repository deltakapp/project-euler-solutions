# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def largestPrimeFactor(target):
  factors = [] # holds prime factors
  candidate = 2 # first candidate for a prime factor (2 is smallest prime)
  root = math.sqrt(target) # used as a loop limiter to reduce computational complexity

  # if target is divisible by candidate, add candidate to list of factors and
  # recalculate target and root
  def check(candidate):
    nonlocal target
    while target % candidate == 0: #
      factors.append(candidate)
      target = target / candidate
      root = math.sqrt(target)

  check(candidate) # check 2, which is the smallest prime
  candidate = 3 # increment candidate to 3, which is the nest prime
  while candidate <= root:
    check(candidate)
    candidate += 2 # increment to the next odd int (2 is the only even prime)
  
  return factors[-1]

print(largestPrimeFactor(600851475143))
