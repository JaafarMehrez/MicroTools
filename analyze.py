from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.io.cif import CifParser

# Specify the path to your CIF file
cif_file = "graphene.cif"

# Create a CifParser object
parser = CifParser(cif_file)

# Parse the structures with the new method and set primitive=True explicitly
structures = parser.parse_structures(primitive=True)

# Access the first structure
structure = structures[0]

# Create a SpacegroupAnalyzer object for the crystal structure
analyzer = SpacegroupAnalyzer(structure)

# Get the spacegroup number and symbol
spacegroup_number = analyzer.get_space_group_number()
spacegroup_symbol = analyzer.get_space_group_symbol()

# Print the spacegroup information
print("Spacegroup Number:", spacegroup_number)
print("Spacegroup Symbol:", spacegroup_symbol)

# Check if the property of interest is isotropic based on crystal symmetries
is_isotropic = analyzer.is_laue()  # Returns True if the crystal is isotropic

# Print the result
if is_isotropic:
    print("The property of interest is isotropic.")
else:
    print("The property of interest is anisotropic.")
