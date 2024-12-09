import numpy as np
import librosa
from sound_object import Sound


def lpc_max_pos_run(sound: Sound) -> float:
    """
    Calculates the longest run of positive LPC coefficients for a given audio file.
    """
    lpc = librosa.lpc(sound.data, order=13)
    max_run = 0
    current = 0
    for val in lpc:
        if val > 0:
            current += 1
            max_run = max(max_run, current)
        else:
            current = 0
    return max_run
