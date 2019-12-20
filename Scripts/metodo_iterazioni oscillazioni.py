from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = np.linspace(0, 1.1, 1000)
r_valori = [3.3, 3.46, 3.55]
oscillazioni = [2, 4, 8]
nsteps = 100

colors = ['yellowgreen', 'orange', 'firebrick']

for (r,c, o) in zip(r_valori, colors, oscillazioni):
    f = r*x- r*x**2
    seq = [np.array([0.7])]
    for j, s in enumerate(seq):
        for i in range(nsteps):
            s = np.append(s, r*(s[i] - s[i]**2))
        seq[j] = s

    plt.plot(x, f, 'k-', label=r'$f(x) = rx- rx^2$')
    plt.plot(x, x, 'k--', label=r'$y=x$')
    for s in seq:
        y=0
        for i in range(nsteps-3):
            plt.plot([s[i], s[i]], [y, r*(s[i] - s[i]**2)], '-', color=c)
            y = r*(s[i] - s[i]**2)
            if(i==0):
                plt.plot([s[i], y], [y,y], '-', color = c)
            else:
                plt.plot([s[i], y], [y,y], '-', color = c)
                if i >= nsteps - 3 - o:
                    plt.plot(s[i], y, 'o', fillstyle='full', color = 'black', alpha=0.6)

    plt.title(r'Iterazioni per $r=%0.2f$'%(r), fontsize=24)
    plt.xlabel('$x$',fontsize=14)
    plt.ylabel('$y$', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlim(0, 1)
    plt.ylim(0,1)
    plt.legend(loc='lower left', fontsize=16)
    plt.show()