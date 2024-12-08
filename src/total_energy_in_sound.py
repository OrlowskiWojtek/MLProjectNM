import numpy as np
from sound_object import Sound


def normalized_total_energy(sound: Sound) -> float:
    """
    Calculate normalized total energy in sound.
    """

    # Calculate total energy
    energy: float = np.sum(np.square(sound.data))

    return energy / len(sound.data)
