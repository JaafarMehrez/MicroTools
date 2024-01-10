from ase.io import read, write

# Load the initial structure from the POSCAR file
initial_structure = read('path/to/POSCAR')

# Define the range and step size for the applied strain
strain_range = [-0.015, -0.01, -0.005, 0.0, 0.005, 0.01, 0.015]

# Apply axial strain and save the strained structures
for strain in strain_range:
    strained_structure = initial_structure.copy()
    strained_structure.cell[2, 2] *= (1 + strain)  # Apply strain in the z direction
    
    # Save the strained structure to a new POSCAR file
    strained_poscar = f'strained_poscar_{strain:.3f}.vasp'
    write(strained_poscar, strained_structure, format='vasp')
