import numpy as np
from sound_object import Sound

def fit_3rd_polynomial(sound:Sound):
    """
    Fits to the sound vector a 3rd polynomial
    returns cubic coefficient a 
    ax³+bx²+cx+d
    """
    x=np.linspace(0,len(sound.data),len(sound.data))

    # Fitting a polynomial
    coefficients = np.polyfit(x, np.abs(sound.data), 3)

    return coefficients[0]