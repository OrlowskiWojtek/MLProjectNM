import numpy as np
import librosa
from sound_object import Sound


def lpc_diff(sound: Sound) -> float:
    """
    Calculates the difference between the mean values of the first and second halves of
    the LPC coefficients for a given audio file.
    """
    lpc = librosa.lpc(sound.data, order=13)
    lower = np.mean(lpc[7:])
    higher = np.mean(lpc[:7])
    diff = higher - lower
    return diff
