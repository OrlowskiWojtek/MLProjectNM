import numpy as np
import librosa
from sound_object import Sound


def lpc_stdev(sound: Sound) -> float:
    """
    Calculates the standard deviation of the LPC coefficients for a given audio file.
    """
    lpc = librosa.lpc(sound.data, order=13)
    return np.std(lpc)
