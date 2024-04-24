import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import FormatStrFormatter
from pymatgen.io.vasp import Chgcar

# Read the CHGCAR file
chgcar = Chgcar.from_file("CHGCAR")

# Get the electron density data
electron_density = chgcar.data["total"]

# Get the grid dimensions
grid_dim = chgcar.dim

# Function to validate user-specified plane
def validate_plane(plane, plane_dir):
    if plane_dir == 'x':
        if plane < 0 or plane >= grid_dim[0]:
            raise ValueError("Invalid plane index. Must be between 0 and {}".format(grid_dim[0] - 1))
    elif plane_dir == 'y':
        if plane < 0 or plane >= grid_dim[1]:
            raise ValueError("Invalid plane index. Must be between 0 and {}".format(grid_dim[1] - 1))
    elif plane_dir == 'z':
        if plane < 0 or plane >= grid_dim[2]:
            raise ValueError("Invalid plane index. Must be between 0 and {}".format(grid_dim[2] - 1))
    else:
        raise ValueError("Invalid plane direction. Must be 'x', 'y', or 'z'.")

# Prompt the user for the plane direction
plane_dir = input("Enter the plane direction ('x', 'y', or 'z'): ")
plane_dir = plane_dir.lower()

# Prompt the user for the plane number
plane = int(input("Enter the plane index to plot (0 to {}): ".format(grid_dim[{'x': 0, 'y': 1, 'z': 2}[plane_dir]] - 1)))
validate_plane(plane, plane_dir)

# Create X and Y coordinate grids based on the chosen plane direction
if plane_dir == 'x':
    x = np.arange(grid_dim[1])
    y = np.arange(grid_dim[2])
    X, Y = np.meshgrid(x, y)
    plane_data = electron_density[plane, :, :].T
    xlabel = "Y"
    ylabel = "Z"
elif plane_dir == 'y':
    x = np.arange(grid_dim[0])
    y = np.arange(grid_dim[2])
    X, Y = np.meshgrid(x, y)
    plane_data = electron_density[:, plane, :].T
    xlabel = "X"
    ylabel = "Z"
else:
    x = np.arange(grid_dim[0])
    y = np.arange(grid_dim[1])
    X, Y = np.meshgrid(x, y)
    plane_data = electron_density[:, :, plane].T
    xlabel = "X"
    ylabel = "Y"

# Create a new figure
fig, ax = plt.subplots(figsize=(8, 8))

# Set the font to Georgia
font_path = fm.findfont(fm.FontProperties(family="Georgia"))
font_prop = fm.FontProperties(fname=font_path)

# Plot the contour plot
contour = ax.contour(X, Y, plane_data, colors="black")
ax.set_title(f"Contour Plot of Electron Density (Plane {plane_dir.upper()} = {plane})", fontproperties=font_prop, fontsize=16)
ax.set_xlabel(xlabel, fontproperties=font_prop)
ax.set_ylabel(ylabel, fontproperties=font_prop)
ax.set_aspect("equal")

# Add contour labels with adjusted font size
ax.clabel(contour, inline=True, fmt=FormatStrFormatter("%.2f"), fontsize=12)

# Show the plot
plt.show()
