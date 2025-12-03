import numpy as np
import scipy.special as sp

def angular_wavefunction(l,m,theta,phi):
    """
    This function computes  normalized Real Spherical Harmonic Y_lm(Real) 
    using scipy spherical function and a phase shifting exponential factor

    Here the function take arguments in the order in l , m ,theta and phi as 
    in physics convention .In Physics's convention: theta is polar fucntion(0-pi) and 
    phi is azimuthal (0-2*pi) whereas Scipy's convention: theta is azimuthal(0-2*pi) 
    and phi is polar(0-pi)
     Args:
        m (int): magnetic quantum number
        l (int): azimuthal quantum number
        theta (numpy.ndarray): polar angle
        phi (int): azimuthal angle
    Returns:
        numpy.ndarray: wavefunction angular 
        component
     Mathematical Transformation:
      We convert Complex Y_lm (Eigenfunctions of Lz) to Real Y_lm (Cartesian orbitals).
      Complex: Y_lm ~ P_lm(cos theta) * e^(i*m*phi)
      Real:  Linear combinations of +m and -m to isolate sin(m*phi) and cos(m*phi).
    """
    
    #Case 1: m=0(z-oriented orbitals like p_z ,d_z^2). Here Y_l0 is real.The exponential term is e^0=1
    if m==0:
        Y_Complex = sp.sph_harm(m,l,phi,theta)
        return np.real(Y_Complex)
    
    elif m > 0:
        '''Case 2: m>0(Cosine-like orbitals likep_z, d_x^2-y^2).
        Here we want the real part of complex harmonic.
        formula: Y_real = sqrt(2) * (-1)^m * Re(Y_l^m).
        (-1)^m is Condon-Shortley phase.It ensures the orbitals lobes 
        align with positive axes(Some Quantum chemistry convention)
        P.S: I'm a Physics major , i don't know much about Condon-Shortley 
        phase . I saw it in a textbook'''
        
        Y_Complex = sp.sph_harm(m,l,phi,theta)
        return np.sqrt(2)*np.real(Y_Complex)*((-1)**m)# taking real part for the cosine component.

    else:
        '''Case:3 m<0 (sine-like orbitals like p_y, d_xy)
        Here we want the imaginary complex harmonic 
        formula: Y_real = sqrt(2) * (-1)^m * Im(Y_l^|m|)
        We use abs(m) because Y_l^-m and Y_l^m share the same
        Calculating from positive m is numerically safer and standard.'''
        
        Y_pos=sp.sph_harm(abs(m),l,phi,theta)
        return np.sqrt(2)*np.imag(Y_pos)*((-1)**m)# np.imag to extract sine compoenent.