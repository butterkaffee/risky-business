import numpy as np
from numpy import fft
from math import exp
import distributions

class CollectiveModel(object):

  
  def __init__(self, f, count_distribution):
    """ f = array of schadenhhenverteilung, count_distribution = riskybiz distribution or array """
   
    self.count_distribution = count_distribution
    self.f = f 
   
    if type(self.count_distribution) == distributions.Poisson:
      self.a = 0
      self.b = self.count_distribution.lam
      self.p0 = exp(- self.b)
      self.g = []
      self.g.append(self.p0 * exp(f[0]*b))


  def fit_panjer(self, tol = 0.01):
    """ f has to be a discrete schadenhhenverteilung , count_distribution a distribution out of this package """


    while np.sum(g) < 1 - tol or len(g) < len(f):
      m = len(g)
      s = 0
      for k in range(1,m):
        s = (a + (self.b * k)/m)*f[k]*g[m-k]


      g.append(1/(1 - self.f[0]*self.a) * s)

      



  def fit_fft(self, f, count_distribution = [0.2,0.2,0.2,0.2,0.2] ):
    pass



