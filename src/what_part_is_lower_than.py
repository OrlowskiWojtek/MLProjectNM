
import numpy as np
import librosa as lr
from sound_object import Sound

def what_part_is_lower_than(sound:Sound, threshold_ratio = 0.3):
    # Finds max value (amplitude)
    max_value = np.max(np.abs(Sound.data))
    # Defines critical value
    threshold = threshold_ratio * max_value
    # Number of elements lower than threshold
    lower_than_thresh_number = np.sum(np.abs(Sound.data) <= threshold)
    # Calculates the ratio
    ratio = lower_than_thresh_number / len(Sound.data)
    return ratio
