from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def logistica(r, x):
    return r * x * (1 - x)

iterazioni = 1000
ultime_iterazioni = 80
r = np.linspace(0, 4.0, 10000)
x = 1e-5 # valore iniziale

for i in range(iterazioni):
    x = logistica(r, x)     # calcolo lo stato del sistema alla i-esima iterazione
    if i >= (iterazioni - ultime_iterazioni):       # plotto solo le ultime cento iterazioni
        plt.plot(r, x, ',k', alpha=.1)
plt.xlim(2, 4)
plt.ylim(0,1)
plt.axis('off')
#plt.title('Albero di Feigenbaum', fontsize=28)
plt.show()
# plt.ylabel('$x$', fontsize=18)
# plt.xlabel('$r$', fontsize=18)
# plt.xticks(fontsize=18)
# plt.yticks(fontsize=18)
# plt.xlim(0, 4)
# plt.ylim(0,1)
# #plt.title('Albero di Feigenbaum', fontsize=28)
# plt.show()