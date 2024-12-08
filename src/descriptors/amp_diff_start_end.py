from sound_object import Sound


def amp_diff_start_end(sound: Sound) -> float:
    """
    Returns difference between starting point and ending point in a signal.
    """
    start_amplitude: float = sound.data[0]
    end_amplitude: float = sound.data[-1]

    difference: float = start_amplitude - end_amplitude

    return difference
