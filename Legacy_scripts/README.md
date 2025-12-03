

⚠️ Deprecation Notice

These scripts are archived prototypes. They are preserved here to demonstrate the project's history and the engineering challenges that led to the development of the main hydrogen_engine.

Do not use these files for production. They contain hardcoded logic and mislabeled filenames. Use the CLI tool in the root directory instead.These codes were written by me for my BSc Physics final year project.

During the development of these codes , i thought making these visualization tool.

The Engineering Analysis

The refactoring process identified three critical issues in this codebase:

1. Hardcoded Mathematics

The scripts used explicit trigonometric formulas (e.g., Z = cos(theta) * sin(phi)) instead of a generalized Spherical Harmonic solver.

Problem: This required writing a new Python file for every single quantum state.

Solution: The new Engine uses scipy.special.sph_harm to calculate any $(l, m)$ state dynamically.

2. The "F-Orbital" Labeling Error

During the forensic code review, it was discovered that several f-orbital ($l=3$) scripts contained correct shapes but mismatched filenames due to coordinate swaps in the hardcoded formulas.

File Name

Formula Used

Actual Orbital Plotted

Correct Label

fxyz orbital.py

$\cos(2\phi)$

$z(x^2-y^2)$

$f_{z(x^2-y^2)}$

fy(x^2-z^2) orbital.py

$\sin(2\phi)$

$xyz$

$f_{xyz}$

fx(x2-3y2) orbital.py

$\sin(3\phi)$

$y(3x^2-y^2)$

$f_{y(3x^2-y^2)}$

fy(3y2-y2) orbital.py

$\cos(3\phi)$

$x(x^2-3y^2)$

$f_{x(x^2-3y^2)}$

Note: The new engine resolves this by using verified scipy implementations of Real Spherical Harmonics.

3. Coordinate System Asymmetry

The original Probability Density script (Probability density function plotting.py) utilized arctan(x/z) for the polar angle calculation.

Problem: This restricted the polar angle to $[-\pi/2, \pi/2]$, effectively mirroring the top hemisphere of the atom onto the bottom.

Solution: The new engine utilizes arccos(z/r) to correctly map the full $[0, \pi]$ domain, preserving the asymmetry of directed orbitals (e.g., $d_{xz}$).
