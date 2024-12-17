from sound_object import Sound
from .freq_of_n_max import find_n_maximum

def first_max_to_second_max_freq(sound:Sound):
    first_max = find_n_maximum(sound, 0)
    second_max = find_n_maximum(sound, 1)

    ratio = first_max/second_max
    return ratio
