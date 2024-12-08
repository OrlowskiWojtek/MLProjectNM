from sound_object import Sound
from freq_of_n_max import find_n_maximum

def find_third_maximum(sound:Sound):
    third_max = find_n_maximum(sound, 2)
    return third_max