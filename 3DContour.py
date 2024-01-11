import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from pymatgen.core.structure import Structure
from pymatgen.analysis.energy_models import EwaldElectrostaticModel
from pymatgen.core.periodic_table import Specie

# Create a list of lattice parameters
a_values = np.linspace(2, 4, 20)  # Range of lattice parameter a
b_values = np.linspace(3, 6, 20)  # Range of lattice parameter b

# Create an empty list to store the total energy values
total_energy_values = []

# Loop over the lattice parameters and calculate the total energy for each combination
for a in a_values:
    for b in b_values:
        # Create a simple cubic structure with the given lattice parameters
        structure = Structure.from_spacegroup("P1", lattice=[[a, 0, 0], [0, b, 0], [0, 0, b]], species=[Specie("Cu", 2)], coords=[[0, 0, 0]])

        # Calculate the total energy using the Ewald electrostatic model
        ewald_model = EwaldElectrostaticModel()
        total_energy = ewald_model.get_energy(structure)

        # Append the total energy value to the list
        total_energy_values.append(total_energy)

# Convert the lattice parameters and total energy values to numpy arrays
a_array, b_array = np.meshgrid(a_values, b_values)
energy_array = np.array(total_energy_values).reshape(len(b_values), len(a_values))

# Create a contour plot using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the contour
ax.contour(a_array, b_array, energy_array, cmap=cm.coolwarm)

# Set labels and title
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Total Energy')
ax.set_title('Total Energy vs Lattice Parameters')

# Show the plot
plt.show()
