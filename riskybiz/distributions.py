from math import exp


# exponential distribution
def exponential_density(x, lam=1):
  if x < 0:
    return 0
  else: 
    return lam* exp(-lam * x)