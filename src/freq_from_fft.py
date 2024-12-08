import numpy as np
from sound_object import Sound

def get_frequencies_from_fft(sound:Sound):

    try:
        audio = sound.data
        sr = sound.sr

        fft_result = np.fft.fft(audio)
        
        n = len(audio)
        freq = np.fft.fftfreq(n, d=1/sr)

        amplitudes = np.abs(fft_result)

        positive_freqs = freq[:n//2]
        positive_amplitudes = amplitudes[:n//2]

        return positive_freqs, positive_amplitudes
    except Exception as e:
        print(f"Error calculating FFT: {e}")
        return None, None