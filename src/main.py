from vis import plot_waveform
from load_data import load_sounds_from_directory
from cut_voice import trim_sound

##

dir = "../../recordings"
sounds = load_sounds_from_directory(dir)

##

trimmed = trim_sound(sounds[0])

##

plot_waveform(sounds[0])
plot_waveform(trimmed)

##

