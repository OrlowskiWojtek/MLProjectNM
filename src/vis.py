import librosa as lr
import matplotlib.pyplot as plt
from sound_object import Sound

def plot_waveform(sound:Sound):
    plt.figure()
    lr.display.waveshow(sound.data, sr=sound.sr)
    plt.title(f"Waveform: {sound.file_name}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def plot_spectrogram(sound:Sound):
    plt.figure()
    # Compute Short-Time Fourier Transform (STFT)
    S = lr.stft(sound.data)
    # Convert amplitude to decibels
    S_db = lr.amplitude_to_db(abs(S))
    lr.display.specshow(S_db, sr=sound.sr, x_axis='time', y_axis='log', cmap='magma')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f"Spectrogram: {sound.file_name}")
    plt.show()

