from vis import plot_waveform
from load_data import load_sounds_from_directory
from cut_voice import trim_sound
from noise_reduction import reduce_noise

##

dir = "/home/linuxwojtek/studia/ml/project/recordings"
sounds = load_sounds_from_directory(dir)

##
sound = sounds[50]

reduced = reduce_noise(sound)
trimmed = trim_sound(sound, 0.4)

##
plot_waveform(sound)
plot_waveform(reduced)
plot_waveform(trimmed)

##
import soundfile as sf

sf.write("trimmed_audio_test.wav", trimmed.data, trimmed.sr)
sf.write("audio_test.wav", sound.data, sound.sr)
sf.write("reduced_audio_test.wav", reduced.data, reduced.sr)
