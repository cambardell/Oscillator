import numpy as np
import wave
import struct
import matplotlib.pyplot as plt



def writeToFile(wave_equation, nframes, sampling_rate, file_name):
    file = (file_name + ".wav")

    comptype="NONE"

    compname="not compressed"

    nchannels=1

    sampwidth=2

    max_amplitude = 10000

    wav_file=wave.open(file, 'w')

    wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

    progress = 1
    for s in wave_equation:
        wav_file.writeframes(struct.pack('h', int(s)))
        progress += 1
    print("done")
