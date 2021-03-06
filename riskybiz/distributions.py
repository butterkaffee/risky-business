from math import exp, factorial
import numpy as np
from numpy import vectorize


class Poisson(object):
  
  def __init__(self, lam=None):
    self.lam = lam
    self.name = "Poisson"

  def _pdf(self, k):
    """dont use this directly"""
    return exp(- self.lam) * (self.lam ** k)/ factorial(k)


  def pdf(self, k):
    if type(k) == np.ndarray or type(k) == list:
      vpdf = vectorize(self._pdf)
      return vpdf(k)
    else:
      return self._pdf(k)

  def fit(self,X):
    self.lam = np.mean(X)


# exponential distribution
def exponential_density(x, lam=1):
  if x < 0:
    return 0
  else: 
    return lam* np.exp(-lam * x)

def ev_density(x, a = 1, b= 1, c = 1):
  pass