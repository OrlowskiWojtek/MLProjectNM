import numpy as np
import librosa
from sound_object import Sound

def zero_crossing_rate_mean(sound: Sound) -> float:
    """
    Calculates the mean zero crossing rate for the given sound - Measures how many times the signal changes its sign.
    """
    
    zcr = librosa.feature.zero_crossing_rate(y=sound.data)
    return np.mean(zcr)
