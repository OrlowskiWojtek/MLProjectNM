from vis import plot_waveform
from load_data import load_sounds_from_directory
from cut_voice import trim_sound
from noise_reduction import reduce_noise

import sys
sys.path.append("descriptors/")

from gen_dataframe import generate_dataframe

##

dir = "/home/linuxwojtek/studia/ml/project/recordings"
sounds = load_sounds_from_directory(dir)

for idx in range(len(sounds)):
    sounds[idx] = reduce_noise(sounds[idx])
    sounds[idx] = trim_sound(sounds[idx], 0.4)

df = generate_dataframe(sounds)
print(df)



