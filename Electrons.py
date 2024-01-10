def integrate_chgcar(chgcar_file):
    with open(chgcar_file, 'r') as f:
        lines = f.readlines()

    data_lines = lines[36:]  # Start from line 37

    total_electrons = 0.0
    for line in data_lines:
        values = line.split()
        for value in values:
            try:
                total_electrons += float(value)
            except ValueError:
                pass  # Skip non-numeric values

    return total_electrons

# Provide the path to your CHGCAR file
chgcar_path = 'path_to_your_CHGCAR_file'

total_electrons = integrate_chgcar(chgcar_path)
print("Total number of electrons in the system:", total_electrons)
