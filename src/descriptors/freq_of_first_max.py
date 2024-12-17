from sound_object import Sound
from .freq_of_n_max import find_n_maximum

def find_first_maximum(sound:Sound):
    first_max = find_n_maximum(sound, 0)
    return first_max
