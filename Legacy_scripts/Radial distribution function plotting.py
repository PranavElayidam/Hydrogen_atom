import numpy as np
import matplotlib.pyplot as plt

# Constants
a0 = 1.0  # Bohr radius in atomic units

# Define all radial wavefunctions
def R_1s(r):
    return 2 * (1/a0)**1.5 * np.exp(-r/a0)

def R_2s(r):
    return (1/(2*np.sqrt(2))) * (1/a0)**1.5 * (2 - r/a0) * np.exp(-r/(2*a0))

def R_2p(r):
    return (1/(2*np.sqrt(6))) * (1/a0)**1.5 * (r/a0) * np.exp(-r/(2*a0))

def R_3s(r):
    coeff = 2/(3*np.sqrt(3)) * (1/a0)**1.5
    poly = 1 - (2*r)/(3*a0) + (2*r**2)/(27*a0**2)
    return coeff * poly * np.exp(-r/(3*a0))

# Generate radial distances
r = np.linspace(0, 30, 1000)  # High resolution for accurate integration

# Calculate radial distribution functions
orbitals = {
    '1s': R_1s(r),
    '2s': R_2s(r),
    '2p': R_2p(r),
    '3s': R_3s(r)
}

P = {orbital: 4 * np.pi * r**2 * (wavefunc)**2 for orbital, wavefunc in orbitals.items()}

# Verify normalization using numpy.trapezoid
print("Normalization integrals:")
for orbital, density in P.items():
    integral = np.trapz(density, r)
    print(f"{orbital}: {integral:.4f}")

# Plot settings
plt.figure(figsize=(12, 7))
colors = ['blue', 'green', 'red', 'purple']
linestyles = ['-', '--', '-.', ':']

for (orbital, density), color, ls in zip(P.items(), colors, linestyles):
    plt.plot(r, density, color=color, linestyle=ls, linewidth=2, 
             label=f'{orbital} orbital')

plt.title('Hydrogen Atom Radial Distribution Functions', fontsize=14)
plt.xlabel('Radial Distance (a₀)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, 30)
plt.ylim(0, 6)  # Adjusted for better visual comparison
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
