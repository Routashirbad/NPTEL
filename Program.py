"""
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise.
(If m is not positive, your function should return False.)
"""
#SOLUTION:-
def factor(x):
  factors = []
  for i in range(1,x+1):
    if x % i == 0:
      factors.append(i)
  return factors

def prime(x):
  for i in range(2,x):
    if x % i == 0:
      return False
      break
  else:
      return True

def primepartition(m):
  for i in range(1,m//2+1):
    if prime(i) and prime(m-i):
      return True
  return False
