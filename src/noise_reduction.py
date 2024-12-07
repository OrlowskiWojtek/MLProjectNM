### Different noise reduction algorithms

import librosa
import numpy as np
import noisereduce as nr
from sound_object import Sound

def reduce_noise(sound: Sound):
    y = sound.data
    sr = sound.sr
    
    reduced = nr.reduce_noise(y = y, sr = sr, stationary = True, prop_decrease = 0.75)
    new_sound = Sound(reduced, sr, sound.file_name, sound.gender, sound.word)
    return new_sound

