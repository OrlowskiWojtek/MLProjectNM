from vis import plot_waveform
from load_data import load_sounds_from_directory
from cut_voice import trim_sound
from noise_reduction import reduce_noise

import sys
sys.path.append("descriptors/")

from mean_difference_in_parts import mean_difference

##

dir = "/home/linuxwojtek/studia/ml/project/recordings"
sounds = load_sounds_from_directory(dir)

##
sound = sounds[50]

reduced = reduce_noise(sound)
trimmed = trim_sound(sound, 0.4)

print(mean_difference(sound))

