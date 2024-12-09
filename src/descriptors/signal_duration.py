import librosa
from sound_object import Sound

def signal_duration(sound: Sound) -> float:
    """
    Calculates the duration (time length) of the given sound in seconds.

    Parameters:
        sound (Sound)

    Returns:
        float: The duration of the sound in seconds.
    """
    duration = librosa.get_duration(y=sound.data, sr=sound.sr)
    return duration
