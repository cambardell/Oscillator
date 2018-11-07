import waves
from writeToFile import writeToFile
import matplotlib.pyplot as plt

amp_data = waves.amp_function(10, 48000, 3, 1, 0.6, 3, 3)

writeToFile(waves.sine(440, 10) * amp_data, 10*48000, 48000, "sin")
writeToFile(waves.square(440, 10) * amp_data, 10*48000, 48000, "square")
writeToFile(waves.saw(440, 10) * amp_data, 10*48000, 48000, "saw")
writeToFile(waves.tri(440, 10) * amp_data, 10*48000, 48000, "tri")
