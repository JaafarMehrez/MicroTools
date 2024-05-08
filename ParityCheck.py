import numpy as np

def read_hamiltonian():
    """
    Read hopping matrix elements from the wannier90 output file: wannier90_hr.dat
    wan_num: number of wannier functions
    wsc_num: number of wigner-sitez cells
    wsc_count: variables related to degeneracy
    """

    path = "wannier90_hr.dat"  # Assuming the file is located in the same directory as the script

    with open(path, "r") as f:
        lines = f.readlines()

    wan_num = int(lines[1])
    wsc_num = int(lines[2])
    ski_row_num = int(np.ceil(wsc_num / 15.0))  # skip row numbers
    wsc_count = []
    for i in range(ski_row_num):
        wsc_count.extend(list(map(int, lines[i + 3].split())))

    wsc_tot = np.zeros((wan_num ** 2 * wsc_num, 3))
    tem_tot = np.zeros((wan_num ** 2 * wsc_num, 2))
    for i in range(wan_num ** 2 * wsc_num):
        wsc_tot[i, :] = list(map(int, lines[3 + ski_row_num + i].split()[:3]))
        tem_tot[i, :] = list(map(float, lines[3 + ski_row_num + i].split()[5:]))

    wsc_idx = wsc_tot[0:-1:wan_num ** 2, :]  # the translational vector between wigner-sitez cells
    hop_mat = np.reshape(tem_tot[:, 0] + 1j * tem_tot[:, 1], [wan_num, wan_num, wsc_num], order='F')

    return hop_mat, wsc_idx, wsc_count, wan_num


def calculate_parity(hop_mat, k_point, occupied_band):
    """
    Calculate the parity of the occupied band at a specific k-point in the Brillouin zone.
    hop_mat: hopping matrix
    k_point: k-point coordinates in reciprocal space
    occupied_band: index of the occupied band
    """

    num_bands, _, num_wsc = hop_mat.shape

    # Diagonalize the Hamiltonian at the specific k-point
    ham_k = np.zeros((num_bands, num_bands), dtype=np.complex128)
    for i in range(num_wsc):
        ham_k += np.exp(1j * np.dot(k_point, wsc_idx[i])) * hop_mat[:, :, i]

    eigenvalues, eigenvectors = np.linalg.eig(ham_k)

    # Sort the eigenvalues and eigenvectors in ascending order
    sort_indices = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[sort_indices]
    eigenvectors = eigenvectors[:, sort_indices]

    # Determine the parity of the occupied band
    occupied_eigenvector = eigenvectors[:, occupied_band]
    parity = np.sign(np.vdot(occupied_eigenvector, np.conj(occupied_eigenvector)))

    return parity


if __name__ == "__main__":
    hop_mat, wsc_idx, wsc_count, wan_num = read_hamiltonian()
    print("Hop Matrix (hop_mat):\n", hop_mat)
    print("Wigner-Sitez Cell Indices (wsc_idx):\n", wsc_idx)
    print("Wigner-Sitez Cell Counts (wsc_count):\n", wsc_count)
    print("Number of Wannier Functions (wan_num):\n", wan_num)

    k_point = np.array([0.0, 0.0, 0.0])  # Specify the k-point coordinates, in this case we are choosing Gamma (0,0,0), the center of the BZ
    max_occupied_band = 132  # Specify the index of the last occupied band according to your system

    parities = np.zeros((max_occupied_band + 1, max_occupied_band + 1), dtype=np.float64)

    for band in range(max_occupied_band + 1):
        parity = calculate_parity(hop_mat, k_point, band)
        parities[band, band] = np.real(parity)
        print("Parity of band", band, "at k-point", k_point, ": ", np.real(parity))

    print("Parities Matrix:\n", parities)

    product = np.prod(np.diag(parities))
    print("Product of the diagonal elements in the Parities matrix:", product)
