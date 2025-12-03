# Importing necessary libraries and modules 
import numpy as n # For numerical computations, aliased as 'n'
from matplotlib import cm  # For colormaps
import matplotlib.pyplot as plot  # For plotting, aliased as 'plot'
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Function to convert spherical polar coordinates to Cartesian coordinates
def sphere(r,theta,phi):
    """
    Converts spherical polar coordinates (r, theta, phi) to Cartesian coordinates (x, y, z).
    
    Parameters:
        r (float or np.ndarray): Radial distance.
        theta (float or np.ndarray): Polar angle (angle from the positive z-axis).
        phi (float or np.ndarray): Azimuthal angle (angle in the x-y plane from the positive x-axis).
    
    Returns:
        tuple: Cartesian coordinates (x, y, z).
    """
    x = r*n.sin(theta)*n.cos(phi)
    y = r*n.sin(theta)*n.sin(phi)
    z = r*n.cos(theta)
    return (x,y,z)

# Creating the grid for theta and phi
theta = n.linspace(0,n.pi,1000) # Polar angle from 0 to pi (1000 points)
phi = n.linspace(0,2*n.pi,1000) # Azimuthal angle from 0 to 2pi (1000 points)
theta,phi = n.meshgrid(theta,phi) # Create a 2D grid of (theta, phi) values

# Calculating the d_xy orbital function
Z = (-15/24)*(n.sqrt(14/(5*n.pi)))*(n.sin(theta)*n.sin(theta)*n.sin(theta)*n.cos(3*phi))# Angular part of the orbital

# Converting spherical coordinates to Cartesian coordinates
x,y,z = sphere(n.abs(Z),theta,phi)# Use the absolute value of Z for radial distance

# Setting up the 3D plot
fig = plot.figure() # Create a figure
ax = fig.add_subplot(projection='3d') # Add a 3D subplot

# Adding axes (quivers) to represent the X, Y, and Z axes
axis_length = 0.55  # Length of the axes
ax.quiver(0, 0, 0, axis_length, 0, 0, color='r', label='X-axis', lw=1)  # X-axis
ax.quiver(0, 0, 0, 0, axis_length, 0, color='g', label='Y-axis', lw=1)  # Y-axis
ax.quiver(0, 0, 0, 0, 0, axis_length, color='b', label='Z-axis', lw=1)  # Z-axis

# Plotting the nucleus as a red dot at the origin
ax.scatter(0, 0, 0, color='red', s=100, label='nucleus')  # Red dot at the origin

# Setting plot properties
ax.set_aspect('auto')  # Allow the plot to scale automatically
ax.set_title("f$_{y(3y^{2}-y^{2})}$",fontsize=18) # Set the title
ax.set_xlabel("X") # Label for the X-axis
ax.set_ylabel("Y") # Label for the Y-axis
ax.set_zlabel("Z") # Label for the Z-axis

# Plotting the orbital surface
ax.plot_surface(x,y,z,cmap='winter', alpha =0.7)# Surface plot with winter colormap and transparency

# Adding a legend to identify the axes and nucleus
ax.legend() 

# Turning off the axis for a cleaner look
plot.axis('off')

# Display the plot
plot.show()