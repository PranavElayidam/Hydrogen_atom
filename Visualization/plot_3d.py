import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''Importing the Math Logic.
   Since our file structure puts 'physics' and 'visualization' as 
   neighbor folders inside 'Hydrogen_Engine', we can import directly 
   from physics.angular.
   
   P.S: This only works if you run the program from main.py! 
   If you run this script directly, Python gets lost and can't find 'physics'.'''
try:
    from Physics.angular import angular_wavefunction
except ImportError:
    print("Error: Could not find angular_wavefunction.py. Make sure it's in the Physics folder and Run this from the project root!!")

def render(n, l, m, resolution=100):
    """
    Renders the 3D angular shape. 
    """
    print(f"Rendering 3D Surface for Orbital ({n},{l},{m})...")
    
    '''Step 1: The Grid (The mesh).
       We need to wrap the sphere in a grid of points.
       Think of this like a wireframe globe.
       P.S: I set default resolution to 100. If you go to 200+, 
       Matplotlib gets super laggy and my laptop fans start screaming.'''
    theta_grid = np.linspace(0, np.pi, resolution)
    phi_grid = np.linspace(0, 2 * np.pi, resolution)
    theta, phi = np.meshgrid(theta_grid, phi_grid)

    '''Step 2: The Shape Trick.
       We call our math function to get Y_lm.
       Then we set the radius 'r' equal to the magnitude of Y_lm.
       Because we want the "shape" to bulge out where the probability is high.
       It's a visualization hack, but it's how every textbook does it.'''
    Y_lm = angular_wavefunction(l, m, theta, phi)
    r = np.abs(Y_lm)

    '''Step 3: Coordinate Conversion.
       Computer screens work in x,y,z (Cartesian).
       We have r, theta, phi (Spherical).
       Standard conversion formulas apply here.'''
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    '''Step 4: Painting the Phases.
       We want to see the positive lobes vs negative lobes.
       So we create a color array same shape as our grid.
       Blue = Positive wave, Red = Negative wave.
       Alpha (0.8) makes it slightly see-through so 3D looks better.'''
    phase_colors = np.zeros(Y_lm.shape + (4,))
    
    # Normalize colors for RGBA
    phase_colors[Y_lm > 0] = [0.1, 0.5, 1, 1.0] # Nice Dark Blue
    phase_colors[Y_lm < 0] = [1, 0.2, 0.2, 1.0] # Nice Dark Red

    # Step 5: Plotting
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # rstride/cstride determines how detailed the wireframe is drawn.
    # Higher numbers = coarser look but faster rotation.
    ax.plot_surface(x, y, z, facecolors=phase_colors, 
                    rstride=2, cstride=2, linewidth=0, antialiased=True)
    
    # Making it look pretty (removing axes so it looks like a floating object)
    ax.set_title(f"Orbital Shape (l={l}, m={m})", fontsize=20)
    
    # Fix the zoom so the orbital isn't tiny or clipped
    max_lim = np.max(r)
    ax.set_xlim(-max_lim, max_lim)
    ax.set_ylim(-max_lim, max_lim)
    ax.set_zlim(-max_lim, max_lim)
    
    ax.axis() 
    plt.show()

