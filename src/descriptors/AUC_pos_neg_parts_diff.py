from sound_object import Sound
import numpy as np 

def AUC_diff(sound:Sound):
    data = np.array(sound.data)

    positive_data = data.copy()
    positive_data[positive_data < 0] = 0

    positive_data = positive_data/max(positive_data)

    negative_data = data.copy()
    negative_data[negative_data >= 0] = 0

    negative_data = negative_data/min(negative_data)

    time = np.arange(0, len(sound.data)/sound.sr - 1/sound.sr, 1/sound.sr)
    
    area_pos = np.trapz(positive_data, time)
    area_neg = np.trapz(negative_data, time)

    diff = area_pos - area_neg

    return diff