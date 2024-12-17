from sound_object import Sound
from .freq_from_fft import get_frequencies_from_fft

def find_freq_for_minimum_amp(sound:Sound):

    freq, amp = get_frequencies_from_fft(sound)
    
    amp_croped = amp[amp > max(amp) * 0.1]
    freq_croped = freq[amp > max(amp) * 0.1]

    paired = list(zip(freq_croped, amp_croped))

    if len(freq) < 3:
        return None
    
    paired_sorted = sorted(paired, key=lambda x: x[1], reverse=True)
    
    sorted_freq, sorted_amps = zip(*paired_sorted)
    
    if len(sorted_freq) < 3:
        return None
    
    min = sorted_freq[-1]
    
    return min
