from pymatgen.core.structure import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

# Load the structure from the POSCAR file
structure = Structure.from_file('POSCAR')

# Perform symmetry analysis
finder = SpacegroupAnalyzer(structure)
symmetry_data = finder.get_symmetry_dataset()

# Print the space group symbol and number
print("Space group symbol:", symmetry_data['international'])
print("Space group number:", symmetry_data['number'])
