import numpy as np

mu = 3
sigma = 0.5 
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)

import pandas as pd

df = pd.DataFrame(vals)
print(df.describe())

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=vals, bins=30)
plt.title('Histograma de tiempos de servicio')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

print(bins)
print(count)

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

#Normal (mu=0, sigma=1)
x=np.arange(-4,4-0.001)
plt.plot(x, norm.pdf(x))
plt.title("Densidad normal estadandar")
plt.xlabel("valores")
plt.ylabel("densidad")
plt.show()