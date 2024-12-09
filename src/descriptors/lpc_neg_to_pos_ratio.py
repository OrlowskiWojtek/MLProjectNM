import numpy as np
import librosa
from sound_object import Sound


def lpc_neg_to_pos_ratio(sound: Sound) -> float:
    """
    Calculates the ratio of the negative to positive LPC coefficients for a given audio
    file.
    """
    lpc = librosa.lpc(sound.data, order=13)
    negative_count = np.sum(lpc < 0)
    positive_count = np.sum(lpc > 0)
    if positive_count != 0:
        ratio = negative_count / positive_count
    else:
        ratio = 1
    return ratio
