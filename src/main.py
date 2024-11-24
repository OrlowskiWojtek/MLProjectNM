from vis import plot_waveform
from load_data import load_sounds_from_directory
from cut_voice import trim_sound

##

dir = "../../recordings"
sounds = load_sounds_from_directory(dir)

##

trimmed = trim_sound(sounds[30], 0.4)

##

plot_waveform(sounds[30])
plot_waveform(trimmed)

##
import soundfile as sf

sf.write("trimmed_audio_test.wav", trimmed.data, trimmed.sr)
