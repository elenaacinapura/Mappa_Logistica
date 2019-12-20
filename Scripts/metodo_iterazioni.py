from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc
import math

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

x = np.linspace(0, 1.1, 1000)
r = 1
f = r*x- r*x**2
nsteps = 50


seq = [np.array([0.3]), np.array([0.5]), np.array([0.8]), np.array([0.9])]
for j, s in enumerate(seq):
    for i in range(nsteps):
        s = np.append(s, r*(s[i] - s[i]**2))
    seq[j] = s

colors = ['firebrick', 'royalblue', 'orange', 'red']


plt.plot(x, f, 'k-', label=r'$f(x) = rx- rx^2$')
plt.plot(x, x, 'k--', label=r'$y=x$')
for (c, s) in zip(colors, seq):
    y=0
    for i in range(nsteps-3):
        plt.plot([s[i], s[i]], [y, r*(s[i] - s[i]**2)], '-', color=c)
        y = r*(s[i] - s[i]**2)
        if(i==0):
            plt.plot([s[i], y], [y,y], '-', color = c, label=r'Iterazione da $x_0 = %0.2f$'%(s[0]))
        else:
            plt.plot([s[i], y], [y,y], '-', color = c)
        # if i >= nsteps - 6:
        #     plt.plot(s[i], y, 'o', fillstyle='full', color = 'black', alpha=0.6)
        


plt.title(r'Iterazioni per $r= %s$'%(r), fontsize=24)
plt.xlabel('$x$',fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0, 1)
plt.ylim(0,1)
plt.legend(loc='upper left')
plt.show()