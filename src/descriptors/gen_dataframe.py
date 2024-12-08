import pandas as pd
import numpy as np

from mean_difference_in_parts import mean_difference
from stddev_difference_in_parts import  stddev_difference
from what_part_is_lower_than import what_part_is_lower_than
from where_max_amp import where_max_amp

def generate_dataframe(sounds):
    n_rows = len(sounds)
    n_cols = 4 # number of descriptors
    data = np.zeros((n_rows, n_cols))

    for idx, sound in enumerate(sounds):
        data[idx, 0] = mean_difference(sound)
        data[idx, 1] = stddev_difference(sound)
        data[idx, 2] = what_part_is_lower_than(sound)
        data[idx, 3] = where_max_amp(sound)

    genders = [sound.gender for sound in sounds]
    words = [sound.word for sound in sounds]

    df = pd.DataFrame(data, columns=['mean_difference', 'stddev_difference', 'wpislt', 'wma'])
    df['word'] = words
    df['gender'] = genders

    return df

