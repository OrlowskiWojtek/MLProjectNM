from sound_object import Sound
import numpy as np 

def AUC_with_gaussian_kernel_data(sound:Sound):
    data = np.array(sound.data)

    positive_data = data.copy()
    positive_data[positive_data < 0] = 0

    negative_data = data.copy()
    negative_data[negative_data >= 0] = 0

    time = np.arange(0, len(sound.data)/sound.sr - 1/sound.sr, 1/sound.sr)
    curve = (positive_data + (-negative_data))

    def gaussian_distribution(x, mu=0, sigma=0.15):
        return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    gaussian_kernel = gaussian_distribution(time, mu=max(time)/2)
    gaussian_kernel = gaussian_kernel/max(gaussian_kernel)
    curve = (positive_data + (-negative_data))*gaussian_kernel
    curve = curve/max(curve)

    area = np.trapz(curve, time)

    return area