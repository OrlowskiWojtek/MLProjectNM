import numpy as np
from sound_object import Sound

def fit_4th_polynomial(sound:Sound):
    """
    Fits to the sound vector a 4th polynomial
    returns coefficient a 
    ax^4+bx^3+cx^2+dx+e
    """
    x=np.linspace(0,len(sound.data),len(sound.data))

    # Fitting a polynomial
    coefficients = np.polyfit(x, np.abs(sound.data), 4)

    return coefficients[0]
