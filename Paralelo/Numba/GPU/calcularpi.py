#Motecarlo en Python con Cuda poderoso Cuda Cudaaaaaaaaaa pero en Python

from __future__ import print_function, absolute_import
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random

@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out_d):
    ii = cuda.grid(1)
    cae_adentro = 0

    for i in range(iteraciones):
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)

        if x**2 + y**2 <= 1.0:
            cae_adentro += 1

    out_d[ii] = 4.0 * cae_adentro / iteraciones

#weas de cuda 

hilosporbloque = 64
bloques = 256

seed1 = random.uniform(-1, 1)
seed2 = random.seed(seed1)
seed = random.randint(0, 1000)

rng_states = create_xoroshiro128p_states(hilosporbloque * bloques, seed)
out = np.zeros(hilosporbloque * bloques, dtype = np.float64)
out_d = cuda.to_device(out)

calcularpi_kernel[bloques, hilosporbloque](rng_states, 10000, out_d)
out_d.copy_to_host(out)
print('pi: ', out.mean())
