from sound_object import Sound
import numpy as np 

def AUC_data(sound:Sound):
    data = np.array(sound.data)

    positive_data = data.copy()
    positive_data[positive_data < 0] = 0

    negative_data = data.copy()
    negative_data[negative_data >= 0] = 0

    curve = positive_data + (-negative_data)
    curve = curve/max(curve)
    time = np.arange(0, len(sound.data)/sound.sr - 1/sound.sr, 1/sound.sr)
    
    area = np.trapz(curve, time)

    return area