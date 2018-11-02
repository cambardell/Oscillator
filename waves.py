import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
from writeToFile import writeToFile
from scipy import signal

sampling_rate = 48000.0




def sine(freq, len):
    num_samples = int(len * sampling_rate)

    sine_wave = np.array([np.sin(2 * np.pi * freq * x/sampling_rate) for x in range(num_samples)])
    return sine_wave



def square(freq, len):
    num_samples = int(len * sampling_rate)

    # linspace takes start, stop and number of data points as arguments
    data = np.linspace(0, num_samples, num_samples)



    square_wave = signal.square(2 * np.pi * freq * data)
    return square_wave


def saw(freq, len):
    num_samples = int(len*sampling_rate)

    data = np.linspace(0, num_samples, num_samples)

    saw_wave = signal.sawtooth(2 * np.pi * freq * data)
    return saw_wave


def tri(freq, len):
    num_samples = int(len*sampling_rate)

    data = np.linspace(0, num_samples, num_samples)
    # Second argument is width of the rising ramp as a total proportion of the cycle. Default is 1, 0.5 = triangle
    # because rising and falling half the time.
    tri_wave = signal.sawtooth(2 * np.pi * freq * data, 0.5)
    return tri_wave


def amp_function(len, sampling_rate, attack, decay, sustain, sustain_length, release):
    num_samples = len * sampling_rate
    amp_data = np.zeros(len * sampling_rate)
    for i in range(0, num_samples):
        if i/num_samples < attack/len:
            # amp_data = np.append(amp_data, i*(1/(num_samples*0.3)))
            amp_data[i] = i*(1/(num_samples*0.3))
        elif i/num_samples < attack/len + decay/len:
            # amp_data = np.append(amp_data, i*(-0.4)/48000 + 2.2)
            amp_data[i] = i*(-0.4)/sampling_rate + 2.2
        elif i/num_samples < attack/len + decay/len + sustain_length/len:
            # vamp_data = np.append(amp_data, 0.6)
            amp_data[i] = 0.6
        else:
            # amp_data = np.append(amp_data, i*(-0.6/144000) + 2)
            amp_data[i] = i*(-0.6/144000) + 2

    return amp_data*10000
