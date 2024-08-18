import numpy as np

mu = 3
sigma = 0.5 
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)

import pandas as pd

df = pd.DataFrame(vals)
print(df.describe())