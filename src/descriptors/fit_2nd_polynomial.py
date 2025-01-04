import numpy as np
from sound_object import Sound

def fit_2nd_polynomial(sound:Sound):
    """
    Fits to the sound vector a 2nd polynomial
    returns quadratic coefficient a 
    ax²+bx+c
    """
    x=np.linspace(0,len(sound.data),len(sound.data))

    # Fitting a polynomial
    coefficients = np.polyfit(x, np.abs(sound.data), 2)

    return coefficients[0]