import numpy as np
import scipy.special as sp

def radial_wavefunction(n, l, r, a0=1.0):
    """
    Computes the normalized radial wavefunction R_nl(r).
    Uses Generalized Laguerre Polynomials.
    Args:
        n (int): principal quantum number
        l (int): azimuthal quantum number
        r (array): radial distance
        a0 (float): Bohr radius (default 1.0 for atomic units)
    """
    
    '''Step 0: Sanity Check (Don't break physics).
       We can't have l >= n because angular momentum can't exceed energy level.
       Also n must be positive. If we don't check this, Scipy throws weird errors later.
       P.S: Added this because i kept passing l=2 for n=2 by accident.'''
    if l >= n or n < 1:
        raise ValueError(f"Physics violation: n must be > l. You passed n={n}, l={l}")

    '''Step 1: Generalized Laguerre Polynomials.
       Scipy function takes arguments (order, alpha).
       Physics formula (Griffiths/Shankar) uses L_q^p where q=n-l-1 and p=2l+1.
       So we pass n-l-1 as order and 2l+1 as alpha.
       P.S: Scipy defines Laguerre differently than some math texts, 
       but this matches the Physics convention.'''
    laguerre = sp.genlaguerre(n - l - 1, 2 * l + 1)
    
    # Scaled distance rho. Variable used to make the exponential term unitless
    # WARNING: If a0 is 1.0 (Atomic Units), ensure 'r' is also in atomic units!
    rho = 2 * r / (n * a0)
    
    '''Step 2: Normalization Constant (The messy part).
       Formula: N = sqrt( (2/na0)^3 * (n-l-1)! / (2n * (n+l)!) )
       
       I made a chnage to the formula. I switched to 'gammaln' (Log Gamma) here instead of plain factorial.
       Because if n is large (like n=50), (n+l)! returns 'Infinity' and 
       the code crashes. Logarithms keep the numbers small and safe.
       P.S: I learned it while playing with for very large number for fun.
       I got these solution form Gemini AI (Thank you Google) and verified .Don't worry'''
    
    # We calculate the log of the factorials first: ln(a/b) = ln(a) - ln(b)
    # Note: Gamma(n+1) = n!, so we pass (n-l) for (n-l-1)! and (n+l+1) for (n+l)!
    log_factorial_part = sp.gammaln(n - l) - sp.gammaln(n + l + 1)
    
    prefactor = np.sqrt(
        ((2 / (n * a0)) ** 3) * (1 / (2 * n)) * np.exp(log_factorial_part)
    )
    
    # Final assembly: R_nl(r) = N * exp(-rho/2) * rho^l * L(rho)
    return prefactor * np.exp(-rho / 2) * (rho ** l) * laguerre(rho)