import numpy as np
import matplotlib.pyplot as plt

'''Importing the Math.
   We need the radial logic from the physics folder.
   If you get an error here, you are likely running this script directly 
   instead of running main.py.'''
try:
    from Physics.radial import radial_wavefunction
except ImportError:
    print("Error: Could not find physics module. Make sure it's in the Physics folder and Run this from the project root!!")

def render(n, l):
    """
    Renders the Radial Distribution Function P(r).
    This graph shows 'How likely is it to find the electron at distance r?'
    """
    print(f"Rendering Radial Distribution for n={n}, l={l}...")

    '''Step 1: The Range (How far out do we look?).
       Original code had 40 hardcoded. That was a bad idea.
       If n=1, the electron is at r=1. 40 is way too big (too much empty space).
       If n=10, the electron is at r=100. 40 is way too small (cuts off the graph).
       
       Electron distance scales with n^2 (Basic QM).
       So we set the max distance to roughly 3 * n^2 + 20 just to be safe.'''
    max_r = 3 * n**2 + 20
    r = np.linspace(0, max_r, 1000) 
    
    '''Step 2: Get the raw math.
       We call the function we wrote in physics/radial.py.'''
    R_nl = radial_wavefunction(n, l, r, a0=1.0)
    
    '''Step 3: The Probability Transformation.
       R_nl is just the amplitude.
       |R_nl|^2 is the density at a point.
       
       But we want the Radial Distribution Function P(r).
       P(r) = r^2 * |R|^2.
       
       We use r^2  for a reason . I don't how to explain it technically.
       so i will explain with an example.Imagine an onion skin (shell) at distance r.
       The volume of that thin skin increases as r gets bigger (Volume ~ 4*pi*r^2).
       So even if density (|R|^2) drops, the volume (r^2) grows.
       This explains why the electron is rarely at the nucleus (r=0).'''
    P_r = (r**2) * (np.abs(R_nl)**2)

    '''Step 4: The Plotting.
       Standard matplotlib stuff to make it look nice.'''
    plt.figure(figsize=(10, 6))
    
    # Plot the line
    plt.plot(r, P_r, lw=2, color='purple', label=f'n={n}, l={l}')
    
    # Fill under the curve so it looks like a probability distribution
    plt.fill_between(r, P_r, alpha=0.3, color='purple')
    
    plt.title(f"Radial Distribution Function (n={n}, l={l})")
    plt.xlabel("Distance from Nucleus (Bohr Radii)")
    plt.ylabel("Probability P(r)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()