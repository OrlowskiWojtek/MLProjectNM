import numpy as np
import librosa
from sound_object import Sound

def spectral_flatness_median(sound: Sound) -> float:
    """
    Calculates the median spectral flatness for the given sound.
    """
    
    spectral_flatness = librosa.feature.spectral_flatness(y=sound.data)
    return np.median(spectral_flatness)
