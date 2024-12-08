import numpy as np
from sound_object import Sound


def mean_amplitude(sound: Sound) -> float:
    """
    Calculate mean amplitude of sound.
    """

    # Calculate mean amplitudes
    mean_amp: float = np.mean(np.abs(sound.data))

    return mean_amp
