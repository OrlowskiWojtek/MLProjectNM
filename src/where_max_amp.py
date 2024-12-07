import numpy as np
import librosa as lr
from sound_object import Sound

def where_max_amp(sound:Sound):
    # Finds arg(index) where |val| is max → loudest sound
    max_amplitude_index = np.argmax(np.abs(sound.data))

    # Relative position of max, number in range (0,1]
    location_of_max = (max_amplitude_index + 1)/len(sound.dat)

    return location_of_max
