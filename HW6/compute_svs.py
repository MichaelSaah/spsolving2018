# (1) Hilbert matricies

import numpy as np
import matplotlib.pyplot as plt
from math import sin

size = 100

def gen_mat(size, mat_type):
    for i in range(1, size+1):
        row = []
        for j in range(1, size+1):
            if mat_type == 'hilbert':
                row.append(1/(i+j-1))
            elif mat_type == 'mult':
                row.append(1/(i*j))
            elif mat_type == 'exp':
                row.append(1/(i**j))
            elif mat_type == 'sin':
                row.append(sin(i*j))
        yield row

hilbert_mat = np.array(list(gen_mat(size, 'hilbert')))
mult_mat = np.array(list(gen_mat(size, 'mult')))
exp_mat = np.array(list(gen_mat(size, 'exp')))
sin_mat = np.array(list(gen_mat(size, 'sin')))

_, s_hilbert, _ = np.linalg.svd(hilbert_mat)
_, s_mult, _ = np.linalg.svd(mult_mat)
_, s_exp, _ = np.linalg.svd(exp_mat)
_, s_sin, _ = np.linalg.svd(sin_mat)

plt.semilogy(range(len(s_hilbert)), s_hilbert, 'b.', label='Hilbert')
plt.semilogy(range(len(s_mult)), s_mult, 'r.', label='Multiplicative')
plt.semilogy(range(len(s_exp)), s_exp, 'g.', label='Exponential')
plt.semilogy(range(len(s_exp)), s_sin, 'k.', label='Sin')

plt.legend()
plt.title('Singular Values by Matrix Type, n = ' + str(size))
plt.show()
