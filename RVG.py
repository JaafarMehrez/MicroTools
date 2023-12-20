import numpy as np
from ase.io import read, write
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
surface = read('POSCAR', format='vasp')
temperature = 300.0
np.random.seed(123)

MaxwellBoltzmannDistribution(surface, temperature_K=temperature*units.kB)
print(surface.get_velocities()[:5])
write('modified_POSCAR', surface, format='vasp')
