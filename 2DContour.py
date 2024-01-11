import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pymatgen.core.structure import Structure
from pymatgen.analysis.energy_models import EwaldElectrostaticModel
from pymatgen.core.periodic_table import Specie

# Create a list of lattice parameters
a_values = np.linspace(2, 4, 20)  # Range of lattice parameter a
b_values = np.linspace(3, 6, 20)  # Range of lattice parameter b

# Create an empty 2D array to store the total energy values
total_energy_values = np.zeros((len(a_values), len(b_values)))

# Loop over the lattice parameters and calculate the total energy for each combination
for i, a in enumerate(a_values):
    for j, b in enumerate(b_values):
        # Create a simple cubic structure with the given lattice parameters
        structure = Structure.from_spacegroup("P1", lattice=[[a, 0, 0], [0, b, 0], [0, 0, b]], species=[Specie("Cu", 2)], coords=[[0, 0, 0]])

        # Calculate the total energy using the Ewald electrostatic model
        ewald_model = EwaldElectrostaticModel()
        total_energy = ewald_model.get_energy(structure)

        # Store the total energy value in the 2D array
        total_energy_values[i, j] = total_energy

# Create a meshgrid for the lattice parameters
a_array, b_array = np.meshgrid(a_values, b_values)

# Create the contour plot using matplotlib
fig, ax = plt.subplots()
contour = ax.contourf(a_array, b_array, total_energy_values, cmap=cm.coolwarm)
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_title('Total Energy vs Lattice Parameters')
cbar = fig.colorbar(contour)

# Show the plot
plt.show()
