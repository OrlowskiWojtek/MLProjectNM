import numpy as np
from sound_object import Sound
from freq_from_fft import get_frequencies_from_fft

def find_n_maximum(sound:Sound, n):

    freq, amp = get_frequencies_from_fft(sound)
    paired = list(zip(freq, amp))

    if len(freq) < 3:
        return None
    
    paired_sorted = sorted(paired, key=lambda x: x[1], reverse=True)

    sorted_freq, sorted_amps = zip(*paired_sorted)
    
    if len(sorted_freq) < 3:
        return None
    
    n_max = sorted_freq[n]
    
    return n_max