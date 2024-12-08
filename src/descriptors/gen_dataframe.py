import pandas as pd
import numpy as np

from mean_difference_in_parts import mean_difference
from stddev_difference_in_parts import  stddev_difference
from what_part_is_lower_than import what_part_is_lower_than
from where_max_amp import where_max_amp
from AUC_pos_neg_parts_diff import AUC_diff
from AUC_sound_data import AUC_data
from AUC_with_gaussian_kernel import AUC_with_gaussian_kernel_data
from amp_diff_start_end import amp_diff_start_end
from duration import duration
from first_second_max_ratio import first_max_to_second_max_freq
from freq_of_first_max import find_first_maximum
from freq_of_min_amp import find_freq_for_minimum_amp
from freq_of_n_max import find_n_maximum
from freq_of_second_max import find_second_maximum
from freq_of_third_max import find_third_maximum
from mean_amp import mean_amplitude
from total_energy_in_sound import normalized_total_energy
from zero_crossing_rate import zero_crossing_rate

def generate_dataframe(sounds):
    descriptors = [
        mean_difference,
        stddev_difference,
        what_part_is_lower_than,
        where_max_amp,
        #AUC_diff,
        #AUC_data,
        #AUC_with_gaussian_kernel_data,
        amp_diff_start_end,
        duration,
        first_max_to_second_max_freq,
        find_first_maximum,
        find_freq_for_minimum_amp,
        find_second_maximum,
        find_third_maximum,
        mean_amplitude,
        normalized_total_energy,
        zero_crossing_rate]

    desc_names = [
        "mean_difference",
        "stddev_difference",
        "what_part_is_lower_than",
        "where_max_amp",
        #"AUC_diff",
        #"AUC_data",
        #"AUC_with_gaussian_kernel_data",
        "amp_diff_start_end",
        "duration",
        "first_max_to_second_max_freq",
        "find_first_maximum",
        "find_freq_for_minimum_amp",
        "find_second_maximum",
        "find_third_maximum",
        "mean_amplitude",
        "normalized_total_energy",
        "zero_crossing_rate"]
    n_rows = len(sounds)
    n_cols = len(descriptors) # number of descriptors
    data = np.zeros((n_rows, n_cols))

    for idx, sound in enumerate(sounds):
        for desc_idx, descriptor in enumerate(descriptors):
            data[idx, desc_idx] = descriptor(sound)

    genders = [sound.gender for sound in sounds]
    words = [sound.word for sound in sounds]

    df = pd.DataFrame(data, columns = desc_names)
    df['word'] = words
    df['gender'] = genders

    return df

