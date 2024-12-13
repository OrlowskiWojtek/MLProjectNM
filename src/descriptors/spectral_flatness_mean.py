import numpy as np
import librosa
from sound_object import Sound

def spectral_flatness_mean(sound: Sound) -> float:
    """
    Calculates the mean spectral flatness for the given sound.
    """
    
    spectral_flatness = librosa.feature.spectral_flatness(y=sound.data)
    return spectral_flatness.mean()
