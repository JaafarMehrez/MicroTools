import numpy as np
from ase import Atoms, Atom
from ase.build import fcc111, molecule
from ase.io import write
# Supposed we have Pt surface 
a = 3.92  # Check the correct value of Pt lattice constant in Å
surface = fcc111('Pt', a=a, size=(2, 2, 4), vacuum=10.0, periodic=True)# randomly chosen Pt surface, check for your case or read the surface file if you aiready have one
theta_range = np.linspace(0, np.pi, num=20)  # Range of theta angles (0 to pi), num can change the sampling inside the chosen range
phi_range = np.linspace(0, 2*np.pi, num=40)  # Range of phi angles (0 to 2*pi), same thing about num 
distance_range = np.linspace(0.5, 1, num=10)  # Range of distances (value1 to value2 Å) between the H atoms
# This list is used to store the final xyz files
configurations = []
# Initial trajectories
for theta in theta_range:
    for phi in phi_range:
        for distance in distance_range:
            # Generate H2 molecule with specific distance and orientation
            h2 = molecule('H2')
            h2.set_distance(0, 1, distance)
            h2.rotate(theta, 'y')
            h2.rotate(phi, 'z')
            # Get the positions of H2 atoms relative to Pt surface
            h2_positions = h2.positions + [0.5, 0.5, 2.0 + distance] 
            combined_system = surface.copy()
            combined_system.extend(h2)
            combined_system.positions[-2:] = h2_positions
            configurations.append(combined_system)
# write the final structures XYZ files
for i, configuration in enumerate(configurations):
    filename = f'configuration_{i}.xyz'
    write(filename, configuration, format='xyz') 
