from sound_object import Sound


def duration(sound: Sound) -> float:
    """
    Calculate the duration of a sound in seconds.
    """

    # Get number of samples
    num_samples = len(sound.data)

    # Get sample rate
    sample_rate = sound.srs

    # Calculate the duration basing on number of samples and sample rate
    duration = num_samples / sample_rate

    return duration
