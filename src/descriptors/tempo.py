import numpy as np
import librosa
from sound_object import Sound

def tempo(sound: Sound) -> float:
    """
    Calculates the tempo (beats per minute) for the given sound.
    """
    
    tempo, _ = librosa.beat.beat_track(y=sound.data, sr=sound.sr)
    return tempo
