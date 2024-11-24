import librosa as lr
import os
import sound_object as snd

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

                    gender = snd.Sound.Gender.MALE if("_m_" in file) else snd.Sound.Gender.FEMALE
                    word = snd.Sound.Word.TAK if("_tak_" in file) else snd.Sound.Word.NIE
                    
                    sounds.append(snd.Sound(data, sr, file, gender, word))
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
    return sounds

##

dir = "../../recordings"
sounds = load_sounds_from_directory(dir)

##

for sound in sounds:
    print(f"Filename: {sound.file_name}, sample rate: {sound.sr}")


