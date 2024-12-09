import numpy as np
import librosa
from sound_object import Sound


def mffc_median(sound: Sound) -> float:
    """
    Calculates the median of MFCCs across all time frames for the given sound.
    """
    mfcc = librosa.feature.mfcc(y=sound.data, sr=sound.sr, n_mfcc=13)
    mean_in_time = np.mean(mfcc, axis=1)
    return np.median(mfcc)
