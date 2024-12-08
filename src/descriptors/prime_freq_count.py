import numpy as np
from sound_object import Sound
from freq_from_fft import get_frequencies_from_fft

def count_prime_freqs(sound:Sound):

    freq, amp = get_frequencies_from_fft(sound)

    freq_new = freq[amp > max(amp) * 0.1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = sum(1 for i in set(freq_new) if is_prime(int(i)))/len(set(freq_new))
    
    return prime_count