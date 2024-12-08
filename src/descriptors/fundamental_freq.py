import numpy as np
import librosa as lr
from sound_object import Sound

def calculate_fundamental_frequency(sound:Sound):

    audio = sound.data
    sr = sound.sr

    f0 = lr.yin(audio, fmin=50, fmax=sr//2, sr=sr)

    f0_mean = np.nanmean(f0)

    return f0_mean
