
import numpy as np
import librosa as lr
from sound_object import Sound

def std_difference_difference(sound:Sound, numb_of_div=4):
    # Step 1: Divide the vector into equal parts
    length = len(sound.data)
    segment_size = length // numb_of_div  # Size of each segment
    stddevs = []
    
    # Step 2: Calculate mean of absolute values for each segment
    for i in range(numb_of_div):
        start = i * segment_size
        end = start + segment_size if i < numb_of_div - 1 else length  # Ensure the last segment includes any leftover
        segment = sound.data[start:end]
        stddevs.append(np.std(np.abs(segment)))
    
    # Step 3: Calculate the difference between max and min mean values
    difference = max(stddevs) - min(stddevs)
    return difference
