# Bayes Rule
from pomegranate import *
import numpy
import pandas as pd

X = numpy.load(signal.npy)
df = 
model = BayesianNetwork.from_samples(X, algorithm='exact')
# Need to modify as I have changed the private signal numpy framework
def actual(int blue, int red):
  double b = blue / 100
  double r = red / 100
  double actual  = (b * r) * 2
  return actual
def report(int bluet, int redt):
  double br = bluet
  double rr = redt
  return P(rr, actual(bluet, redt))
m = 1;
for x in X:
  buff = report(X.blue, X.red)
  m = m * buff

  
  
  
