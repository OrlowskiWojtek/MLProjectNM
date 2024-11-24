from enum import Enum

class Sound:
    class Gender(Enum):
        MALE = 1
        FEMALE = 2
    
    class Word(Enum):
        TAK = 1
        NIE = 2

    def __init__(self, data, sr, file_name, gender, word):
        self.data = data       # Audio time series
        self.sr = sr           # Sampling rate
        self.file_name = file_name  # File name
        self.gender = gender
        self.word = word
