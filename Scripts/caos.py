from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

r = 4
n_iterazioni = 50

x0 = 0.3
eps = 1e-6
x1 = x0 + eps

x0_ev = np.array([x0])
x1_ev = np.array([x1])

for i in range(n_iterazioni):
    x0_ev = np.append(x0_ev, r*(x0_ev[-1] - x0_ev[-1]**2))
    x1_ev = np.append(x1_ev, r*(x1_ev[-1] - x1_ev[-1]**2))

plt.plot(np.arange(n_iterazioni), x0_ev[:50], '.-', color = 'black', label=r'$x_0 =$ %0.1f'%(x0))
plt.plot(np.arange(n_iterazioni), x1_ev[:50], '.--', color = 'black', label=r'$x_0  =$ %0.1f$+ 10^{-6}$'%(x0))
plt.title(r'\textbf{Dipendenza dalle condizioni iniziali}', fontsize=24)
plt.xlabel('Iterazione',fontsize=14)
plt.ylabel(r'$f(x) = 4 x(1-x^2)$', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0, n_iterazioni)
plt.legend(loc='lower left')
plt.show()
