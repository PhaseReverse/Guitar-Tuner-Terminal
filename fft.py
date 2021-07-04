import numpy as np

def frequency(data,sampleRate):
    fftVals = np.abs(np.fft.fft(data))
    freqs = np.array(range(0,len(fftVals)))*(sampleRate/len(fftVals))
    frequency = fftVals[0]
    index = 0
    for i in range(int(len(freqs)/2)):
        if fftVals[i] > frequency:
            frequency = fftVals[i]
            index = i
    return freqs[index]




