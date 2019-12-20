import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = np.linspace(0, 1, 1000)
r_valori = [0.5, 1, 2, 3, 3.7]
linestyles = ['-', '--', '-.', ':', (0, (3, 5, 1, 5))]

plt.plot(x, x, '-', color='firebrick')
for r, style in zip(r_valori, linestyles):
    plt.plot(x, r*x*(1-x), 'k', linestyle=style, label=r'$r=$%0.1f'%(r))
plt.xlim(0,1)
plt.ylim(0,1)
plt.title(r'Curve logistiche per $0\leq r \leq 1$', fontsize=24)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend()
plt.show()