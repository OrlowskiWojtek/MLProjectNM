
import numpy as np
import librosa as lr
from sound_object import Sound

def trim_sound(sound:Sound, threshold_ratio = 0.33):
    max_amplitude = np.max(np.abs(sound.data))

    # Set the amplitude threshold
    threshold = threshold_ratio * max_amplitude

    # Find indices of samples above the threshold
    high_amp_indices = np.where(np.abs(sound.data) >= threshold)[0]

    if high_amp_indices.size == 0:
        print("dupa")
        return sound

    # Trim the audio, keeping only the selected portion
    start_idx, end_idx = high_amp_indices[0], high_amp_indices[-1]
    trimmed_data = sound.data[start_idx:end_idx + 1]

    new_sound = Sound(trimmed_data, sound.sr, sound.file_name, sound.gender, sound.word)

    return new_sound

