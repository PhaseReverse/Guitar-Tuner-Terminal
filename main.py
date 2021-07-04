import recorder
import fft
import music_note

while(True):
    data,rate = recorder.record()
    
    music_note.note_status(fft.frequency(data,rate))