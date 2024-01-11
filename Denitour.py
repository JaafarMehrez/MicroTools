import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from pymatgen.io.vasp import Chgcar

# Read the CHGCAR file
chgcar = Chgcar.from_file("CHGCAR")

# Get the electron density data
electron_density = chgcar.data["total"]

# Get the grid dimensions
grid_dim = chgcar.dim

# Define the number of planes to plot
num_planes = 4

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Contour Plots of Electron Density", fontsize=16)

# Loop over the planes and plot each one
for i, ax in enumerate(axs.flat):
    # Choose the plane for plotting
    plane = i * (grid_dim[2] // num_planes)

    # Get the electron density data for the chosen plane
    plane_data = electron_density[:, :, plane]

    # Create X and Y coordinate grids
    x = np.arange(grid_dim[0])
    y = np.arange(grid_dim[1])
    X, Y = np.meshgrid(x, y)

    # Plot the contour plot
    contour = ax.contour(X, Y, plane_data.T, colors="black")
    ax.set_title(f"Plane {plane}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")

    # Add contour labels
    ax.clabel(contour, inline=True, fmt=FormatStrFormatter("%.2f"))

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()
