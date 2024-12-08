import numpy as np
import librosa
from sound_object import Sound


def zero_crossing_rate(sound: Sound) -> float:
    """
    Calculate average value of Zero-Crossing Rate (ZCR).
    """

    # Calculate Zero-Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y=sound.data)

    return np.mean(zcr)
