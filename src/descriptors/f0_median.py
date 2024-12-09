import numpy as np
import librosa
from sound_object import Sound

def f0_median(sound: Sound) -> float:
    """
    Calculates the median fundamental frequency (f0) for the given sound.

    Parameters:
        sound (Sound)

    Returns:
        float: The median f0 value or 'n/a' if no voiced frames are detected.
    """

    f0, voiced_flag, _ = librosa.pyin(
        sound.data, 
        fmin=50,  
        fmax=300,  
        sr=sound.sr
    )
    
    if voiced_flag.any():
        return np.median(f0[voiced_flag])
    else:
        return 'n/a'
