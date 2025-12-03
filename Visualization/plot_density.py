import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''Importing the Math.
   We need the two parts of the wavefunction we wrote earlier.
   If these imports fail, you are probably running this script from the wrong folder.
   Run 'main.py' instead of running this file directly.'''
try:
    from Physics.angular import angular_wavefunction
    from Physics.radial import radial_wavefunction
except ImportError:
    print("Error: Can't find the physics modules. Make sure it's in the Physics folder and Run this from the project root!!")

def render(n, l, m, resolution=800, range_a0=None):
    """
    Renders the 2D Probability Density Heatmap in the XZ plane.
    Basically: Taking a slice through the middle of the atom.
    """
    print(f"Rendering 2D Density Map for ({n},{l},{m})...")

    '''Step 1: The Canvas (Grid Setup).
       We are looking at a slice of the atom (XZ plane).
       Imagine cutting an orange in half. We need coordinates for that flat surface.
       
       P.S: If range_a0 is not set, I'll guess a good zoom level based on n.
       Larger n = bigger atom = we need to zoom out more.'''
    if range_a0 is None:
        range_a0 = 5 * n * n  # A rough heuristic: radius scales with n^2
    
    # Create a square grid of points
    lin = np.linspace(-range_a0, range_a0, resolution)
    x, z = np.meshgrid(lin, lin)
    
    # We are slicing XZ plane, so Y is always 0.
    y = 0

    '''Step 2: The Coordinate Swap.
       Computer screens use X,Z (Cartesian).
       Physics equations use r, theta, phi (Spherical).
       We just convert them here. No fancy math, just geometry.'''
    r = np.sqrt(x**2 + z**2)
    
    # Theta is the angle from top (Z axis).
    # We clip z/r to stay between -1 and 1 so arccos doesn't crash.
    eps = 1e-10
    theta = np.arccos(np.clip(z / (r + eps), -1, 1))
    
    # Phi is the angle around the middle. 
    # Since we are on a flat slice (XZ), right side is 0, left side is Pi.
    phi = np.where(x >= 0, 0, np.pi)

    '''Step 3: The Assembly.
       We grab the Radial part (how far from center) and Angular part (the shape).
       Multiply them together to get the Wavefunction (Psi).'''
    R_nl = radial_wavefunction(n, l, r, a0=1.0)
    Y_lm = angular_wavefunction(l, m, theta, phi)
    
    psi = R_nl * Y_lm
    
    '''Step 4: The Physics to Visuals part.
       Wavefunction (Psi) can be negative.
       Probability Density is Psi squared (always positive).
       This tells us where the electron actually is.'''
    density = np.abs(psi)**2

    '''Step 5: The Plotting.
       We use a Heatmap.
       We plot sqrt(density) instead of raw density.
       Because electron density fades SUPER fast. If we didn't use sqrt,
       you would only see a tiny dot in the center and nothing else.'''
    fig, ax = plt.subplots(figsize=(10, 8))
    
    im = ax.imshow(np.sqrt(density), cmap='rocket', origin='lower',
                   extent=[-range_a0, range_a0, -range_a0, range_a0])
    
    # Making it look understandable
    ax.set_title(f"Electron Density Cross-Section (n={n}, l={l}, m={m})")
    ax.set_xlabel("x (Bohr Radii)")
    ax.set_ylabel("z (Bohr Radii)")
    
    # Add a colorbar so we know what 'bright' means
    plt.colorbar(im, label="Relative Probability (Sqrt scale)")
    plt.show()