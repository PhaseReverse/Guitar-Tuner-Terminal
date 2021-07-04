import sounddevice as sd
import numpy as np


RATE = 44100
CHUNK = 0.5  #Record every 0.5 seconds
CHANNELS = 1

def record(rate = RATE,channel = CHANNELS, time = CHUNK):
    recording = sd.rec(int(time * rate), samplerate = RATE, channels = channel)
    sd.wait()

    recording_final = []
    for i in range(len(recording)):     
 
        recording_final.append(recording[i][0])
        
    
    return np.array(recording_final) , RATE


