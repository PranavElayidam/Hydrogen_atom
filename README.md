Hydrogen Atom Visualization Suite

A comprehensive Python visualization engine that numerically solves the Schrödinger equation for the Hydrogen atom. Unlike standard libraries that often default to complex-valued outputs, this engine explicitly implements Real Spherical Harmonics to render the "textbook" orbital shapes used in chemistry and physics.

🚀 Project Evolution (The Engineering Journey)

This project consists of two distinct stages of development, demonstrating the transition from "Scripting" to "Software Engineering."

The Hydrogen Engine (hydrogen_engine/): The current, production-ready implementation. It features a modular architecture, a unified Command Line Interface (CLI), and a generalized math kernel that calculates any quantum state $(n, l, m)$ on the fly.

Legacy Prototypes (legacy_scripts/): The original hardcoded scripts. Kept for archival purposes to demonstrate the refactoring process and the limitations of non-scalable code.

✨ Features (The Engine)

1. 3D Orbital Isosurfaces

Renders the angular geometry of electron orbitals using a wireframe-over-glass aesthetic.

Math: Implements linear combinations of Spherical Harmonics ($Y_{lm}$) to resolve complex outputs into Real forms (e.g., $p_x, p_y, d_{x^2-y^2}$).

Visuals: Automatic phase coloring (Blue/Red for $\pm$ signs) and aspect ratio correction.

2. 2D Probability Density Heatmaps

Visualizes the internal structure of the atom via a cross-section of the electron probability density ($|\psi|^2$).

Math: Correctly handles spherical coordinate transformations ($\theta = \arccos(z/r)$) to ensure phase symmetry.

Analysis: Reveals radial nodes hidden by 3D surface plots.

3. Radial Distribution Analysis

Plots the probability $P(r)$ of finding an electron at distance $r$ from the nucleus.

Math: Numerical integration of Generalized Laguerre Polynomials.

🛠️ Installation

Clone the repository:

git clone [https://github.com/YOUR_USERNAME/hydrogen-visualization-suite.git](https://github.com/YOUR_USERNAME/hydrogen-visualization-suite.git)
cd hydrogen-visualization-suite


Install dependencies:

pip install -r requirements.txt


🖥️ Usage

The project is controlled via a central CLI in hydrogen_engine/main.py.

1. Visualize a 3D Orbital Shape

# Example: 3d orbital (l=2, m=0)
python hydrogen_engine/main.py shape -l 2 -m 0


2. Visualize 2D Probability Density

# Example: 4f orbital cross-section
python hydrogen_engine/main.py density -n 4 -l 3 -m 0


3. Radial Distribution Graph

# Example: 3s orbital
python hydrogen_engine/main.py radial -n 3 -l 0


🧮 Mathematical Implementation

The engine constructs the full wavefunction $\psi_{nlm}(r,\theta,\phi)$ by combining:

Radial Component ($R_{nl}$):
Computed using scipy.special.genlaguerre.
$$ R_{nl}(r) \propto e^{-\rho/2} \rho^l L_{n-l-1}^{2l+1}(\rho) $$

Angular Component ($Y_{lm}$):
Computed using scipy.special.sph_harm, with a custom wrapper to enforce Real Linear Combinations:

$m=0$: $\text{Re}(Y_{l0})$

$m>0$: $\frac{1}{\sqrt{2}} (Y_{l,-m} + (-1)^m Y_{lm})$

$m<0$: $\frac{i}{\sqrt{2}} (Y_{l,-|m|} - (-1)^m Y_{l|m|})$

📂 Directory Structure

.
├── hydrogen_engine/          # THE NEW CORE (Modular Logic)
│   ├── physics/              # Math Kernel (Angular & Radial logic)
│   ├── visualization/        # Plotting Engines (Matplotlib/3D)
│   └── main.py               # CLI Entry Point
│
├── legacy_scripts/           # THE OLD CODE (Hardcoded Prototypes)
│   └── (Individual scripts for s, px, py, etc.)
│
└── requirements.txt          # Python Dependencies


📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
