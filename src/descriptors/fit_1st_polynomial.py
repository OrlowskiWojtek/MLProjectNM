import numpy as np
from sound_object import Sound

def fit_1st_polynomial(sound:Sound):
    """
    Fits to the sound vector a 1st polynomial
    returns linear coefficient a 
    ax+b
    """
    x=np.linspace(0,len(sound.data),len(sound.data))

    # Fitting a polynomial
    coefficients = np.polyfit(x, np.abs(sound.data), 1)

    return coefficients[0]