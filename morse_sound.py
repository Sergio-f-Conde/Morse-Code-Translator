#!/usr/bin/python3
#
# Purpose: create sine wave sound for the morse code translator
# 
import numpy as np
from scipy.io.wavfile import write

sample_speed= 44100   #samples per second
freq= 700.0		#Hz
duration= 0.18		#Seconds
total_samples= sample_speed*duration
samples= np.arange(total_samples)

wave= np.sin(2*np.pi*samples*freq / sample_speed)
wave_int= np.int16(wave*32767)
write("morse_dash.wav",sample_speed,wave_int)
