import spglib
from ase.io import read

# Load the POSCAR file using ASE
atoms = read("POSCAR")

# Convert the ASE atoms object to a cell compatible with spglib
cell = (atoms.get_cell(), atoms.get_scaled_positions(), atoms.get_atomic_numbers())

# Get the space group symbol
spacegroup_symbol = spglib.get_spacegroup(cell)

# Get the symmetry operations
symmetry = spglib.get_symmetry(cell)
symmetry_operations = symmetry['rotations']
translation_vectors = symmetry['translations']

# Check for various spatial symmetries
has_translation_symmetry = False
has_rotation_symmetry = False
has_reflection_symmetry = False
has_inversion_symmetry = False
has_glide_reflection_symmetry = False
has_mirror_symmetry = False

for operation in symmetry_operations:
    # Check for translation symmetry
    if (operation == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]).all():
        has_translation_symmetry = True

    # Check for rotation symmetry
    if (operation != [[1, 0, 0], [0, 1, 0], [0, 0, 1]]).all():
        has_rotation_symmetry = True

    # Check for reflection symmetry
    if (-1 in operation):
        has_reflection_symmetry = True

    # Check for inversion symmetry
    if -1 in operation.flatten():
        has_inversion_symmetry = True

    # Check for glide reflection symmetry
    if (-1 in operation) and (operation != [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]).all():
        has_glide_reflection_symmetry = True

    # Check for mirror symmetry
    if (operation == [[1, 0, 0], [0, 1, 0], [0, 0, -1]]).all():
        has_mirror_symmetry = True

# Print the full report
print("Structure Report:")
print("Space Group Symbol:", spacegroup_symbol)
print("Has Translation Symmetry:", has_translation_symmetry)
print("Has Rotation Symmetry:", has_rotation_symmetry)
print("Has Reflection Symmetry:", has_reflection_symmetry)
print("Has Inversion Symmetry:", has_inversion_symmetry)
print("Has Glide Reflection Symmetry:", has_glide_reflection_symmetry)
print("Has Mirror Symmetry:", has_mirror_symmetry)
print("Symmetry Operations:")
for i, operation in enumerate(symmetry_operations):
    print("Operation", i+1)
    print("Rotation Matrix:")
    print(operation)
    print("Translation Vector:")
    print(translation_vectors[i])
