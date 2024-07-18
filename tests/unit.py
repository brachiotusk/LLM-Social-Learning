import numpy
import scipy 
import scikit
import math.util
from pomegranate.bayesian_network import *

model = BayesianNetwork.from_samples(df.to_numpy(), state_names=df.columns.values, algorithm='exact')

# Would it be possible to understand how LLM's derive their personal information other than a prompt in a regular situation
