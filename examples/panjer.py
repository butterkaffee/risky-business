import numpy as np 
from riskybiz.collective_model import CollectiveModel 
from riskybiz.distributions import Poisson
import matplotlib.pylab as plt

p = Poisson().fit([2, 3 ,6 ,9, 10])

f = [0.2, 0.2, 0.2, 0.2, 0.2]

cm = CollectiveModel(f, p)

cm.fit_panjer()

print cm.g