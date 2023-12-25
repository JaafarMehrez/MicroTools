from pymatgen.core.structure import Structure
from pymatgen.io.vasp import Poscar
from pymatgen.core.surface import SlabGenerator
import os

# Get the current working directory
cwd = os.getcwd()

# Specify the CONTCAR file name
contcar_file = "CONTCAR"

# Specify the Miller index and added vacuum
miller_index = (1, 0, 0)  # Example: (h, k, l)
vacuum_thickness = 15.0  # Example: Angstroms
min_vacuum_size = 15.0  # Example: Angstroms

# Read the CONTCAR file and generate the surface slab
contcar_path = os.path.join(cwd, contcar_file)
poscar = Poscar.from_file(contcar_path)
structure = poscar.structure
slab_generator = SlabGenerator(structure, miller_index, vacuum_thickness, min_vacuum_size)
slab = slab_generator.get_slab()

# Write the generated slab to a POSCAR file
slab.to("poscar", "POSCAR")
