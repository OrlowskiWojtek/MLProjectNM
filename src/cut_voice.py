
import numpy as np
import librosa as lr
from sound_object import Sound

def trim_sound(sound:Sound):
    threshold_ratio = 0.33
    S_db = lr.amplitude_to_db(abs(sound.data))
    max_db = np.max(S_db)
    db_threshhold = max_db * threshold_ratio

    trimmed_data, _ = lr.effects.trim(sound.data, top_db=db_threshhold)  

    new_sound = Sound(trimmed_data, sound.sr, sound.file_name, sound.gender, sound.word)
    # Trim the audio, keeping only the selected portion
    return new_sound

