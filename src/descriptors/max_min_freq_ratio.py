from sound_object import Sound
from freq_of_n_max import find_n_maximum
from freq_of_min_amp import find_freq_for_minimum_amp

def max_to_min_freq(sound:Sound):
    first_max = find_n_maximum(sound, 0)
    min_freq = find_freq_for_minimum_amp(sound)
    ratio = first_max/min_freq
    return ratio