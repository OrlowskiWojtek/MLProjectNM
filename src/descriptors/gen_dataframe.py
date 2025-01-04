import pandas as pd
import numpy as np

from .AUC_pos_neg_parts_diff import AUC_diff
from .AUC_sound_data import AUC_data
from .AUC_with_gaussian_kernel import AUC_with_gaussian_kernel_data
from .amp_diff_start_end import amp_diff_start_end
from .duration import duration
from .f0_mean import f0_mean
from .f0_median import f0_median
from .first_second_max_ratio import first_max_to_second_max_freq
from .fit_1st_polynomial import fit_1st_polynomial
from .fit_2nd_polynomial import fit_2nd_polynomial
from .fit_3rd_polynomial import fit_3rd_polynomial
from .fit_4th_polynomial import fit_4th_polynomial
from .freq_of_first_max import find_first_maximum
from .freq_of_min_amp import find_freq_for_minimum_amp
from .freq_of_second_max import find_second_maximum
from .freq_of_third_max import find_third_maximum
from .fundamental_freq import calculate_fundamental_frequency
from .lpc_diff import lpc_diff
from .lpc_max_neg_run import lpc_max_neg_run
from .lpc_max_pos_run import lpc_max_pos_run
from .lpc_mean import lpc_mean
from .lpc_neg_to_pos_ratio import lpc_neg_to_pos_ratio
from .lpc_stdev import lpc_stdev
from .max_min_freq_ratio import max_to_min_freq
from .mean_amp import mean_amplitude
from .mean_difference_in_parts import mean_difference
from .mffc_mean import mffc_mean
from .mffc_median import mffc_median
from .mffc_stdev import mffc_stdev
from .prime_freq_count import count_prime_freqs
from .spectral_flatness_mean import spectral_flatness_mean
from .spectral_flatness_median import spectral_flatness_median
from .stddev_difference_in_parts import  stddev_difference
from .tempo import tempo
from .total_energy_in_sound import normalized_total_energy
from .what_part_is_lower_than import what_part_is_lower_than
from .where_max_amp import where_max_amp
from .zero_crossing_rate import zero_crossing_rate
from .zero_crossing_rate_mean import zero_crossing_rate_mean

def generate_dataframe(sounds):
    descriptors = [
        AUC_diff,
        AUC_data,
        AUC_with_gaussian_kernel_data,
        amp_diff_start_end,
        duration,
        f0_mean,
        f0_median,
        first_max_to_second_max_freq,
        fit_1st_polynomial,
        fit_2nd_polynomial,
        fit_3rd_polynomial,
        fit_4th_polynomial,
        find_first_maximum,
        find_freq_for_minimum_amp,
        find_second_maximum,
        find_third_maximum,
        calculate_fundamental_frequency,
        lpc_diff,
        lpc_max_neg_run,
        lpc_max_pos_run,
        lpc_mean,
        lpc_neg_to_pos_ratio,
        lpc_stdev,
        max_to_min_freq,
        mean_amplitude,
        mean_difference,
        mffc_mean,
        mffc_median,
        mffc_stdev,
        count_prime_freqs,
        spectral_flatness_mean,
        spectral_flatness_median,
        stddev_difference,
        tempo,
        normalized_total_energy,
        what_part_is_lower_than,
        where_max_amp,
        zero_crossing_rate,
        zero_crossing_rate_mean]

    desc_names = [
        "AUC_diff",
        "AUC_data",
        "AUC_with_gaussian_kernel_data",
        "amp_diff_start_end",
        "duration",
        "f0_mean",
        "f0_median",
        "first_max_to_second_max_freq",
        "fit_1st_polynomial",
        "fit_2nd_polynomial",
        "fit_3rd_polynomial",
        "fit_4th_polynomial",
        "find_first_maximum",
        "find_freq_for_minimum_amp",
        "find_second_maximum",
        "find_third_maximum",
        "calculate_fundamental_frequency",
        "lpc_diff",
        "lpc_max_neg_run",
        "lpc_max_pos_run",
        "lpc_mean",
        "lpc_neg_to_pos_ratio",
        "lpc_stdev",
        "max_to_min_freq",
        "mean_amplitude",
        "mean_difference",
        "mffc_mean",
        "mffc_median",
        "mffc_stdev",
        "count_prime_freqs",
        "spectral_flatness_mean",
        "spectral_flatness_median",
        "stddev_difference",
        "tempo",
        "normalized_total_energy",
        "what_part_is_lower_than",
        "where_max_amp",
        "zero_crossing_rate",
        "zero_crossing_rate_mean"]

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

