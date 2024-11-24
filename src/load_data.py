import librosa as lr
import os
from sound_object import Sound

##

def load_sounds_from_directory(directory_path, file_extensions=('.wav')):
    """
    Load all audio files in a directory and save them as Sound objects.

    Parameters:
        directory_path (str): Path to the directory containing audio files.
        file_extensions (tuple): Tuple of valid file extensions to consider as audio files.

    Returns:
        list[Sound]: List of Sound objects containing audio data, sampling rate, and metadata.
    """
    sounds = []
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(file_extensions):  # Check for valid audio file
                file_path = os.path.join(root, file)
                try:
                    data, sr = lr.load(file_path, sr=None)  # sr=None to preserve original rate

                    gender = Sound.Gender.MALE if("_m_" in file) else Sound.Gender.FEMALE
                    if("_tak_" in file):
                        word = Sound.Word.TAK
                    elif("_nie_" in file):
                        word = Sound.Word.NIE
                    elif("_rand_" in file):
                        word = Sound.Word.RAND
                    else:
                        word = Sound.Word.ERROR
                        
                    sounds.append(Sound(data, sr, file, gender, word))
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
    return sounds
