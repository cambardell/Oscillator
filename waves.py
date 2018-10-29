import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
from writeToFile import writeToFile
from scipy import signal

sampling_rate = 48000.0
amplitude = 10000
attack = 3
decay = 1
sustain = 0.6
sustain_length = 3
release = 3
max_amplitude = 10000
len = 10



def sine(freq, len):
    num_samples = int(len * sampling_rate)

    amp_data = np.array([])
    for i in range(num_samples):
        if i/num_samples < attack/len:
            amp_data = np.append(amp_data, i*(1/(num_samples*0.3)))
        elif i/num_samples < attack/len + decay/len:
            amp_data = np.append(amp_data, i*(-0.4)/48000 + 2.2)
        elif i/num_samples < attack/len + decay/len + sustain_length/len:
            amp_data = np.append(amp_data, 0.6)
        else:
            amp_data = np.append(amp_data, i*(-0.6/144000) + 2)

    plt.plot(amp_data)
    plt.show()
    amp_data = amp_data*max_amplitude



    sine_wave = np.array([np.sin(2 * np.pi * freq * x/sampling_rate) for x in range(num_samples)])
    sine_wave = sine_wave * amp_data

    writeToFile(sine_wave, num_samples, sampling_rate, "sin")

def square(freq, len):
    num_samples = int(len * sampling_rate)

    # linspace takes start, stop and number of data points as arguments
    data = np.linspace(0, num_samples, num_samples)

    square_wave = signal.square(2 * np.pi * freq * data)
    writeToFile(square_wave, num_samples, sampling_rate, amplitude, "square")

def saw(freq, len):
    num_samples = int(len*sampling_rate)

    data = np.linspace(0, num_samples, num_samples)

    saw_wave = signal.sawtooth(2 * np.pi * freq * data)
    writeToFile(saw_wave, num_samples, sampling_rate, amplitude, "sawtooth")

def tri(freq, len):
    num_samples = int(len*sampling_rate)

    data = np.linspace(0, num_samples, num_samples)
    # Second argument is width of the rising ramp as a total proportion of the cycle. Default is 1, 0.5 = triangle
    # because rising and falling half the time.
    tri_wave = signal.sawtooth(2 * np.pi * freq * data, 0.5)
    writeToFile(tri_wave, num_samples, sampling_rate, amplitude, "triangle")
