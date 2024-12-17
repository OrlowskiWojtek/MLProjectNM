from sound_object import Sound
from .freq_of_n_max import find_n_maximum

def find_second_maximum(sound:Sound):
    second_max = find_n_maximum(sound, 1)
    return second_max
