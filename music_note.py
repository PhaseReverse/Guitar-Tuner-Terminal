#  C4 C#4 D4 D#4 E4 F4 F#4 G4 G#4   A4  Bb4 B4  C5 C#5 D5 D#5 E5 F5 F#5 G5 G#5  A5  Bb5 B5 C6
#                                   f0
#                                   440                                             
#  (fn/f0) =  (a^n)
#  a = 2^(1/12)            


import math

F0 = 440
a = math.pow(2,(1/12))

notes =          ['A','Bb','B','C','C#','D','D#','E','F','F#','G','G#']

notes_subscript = [4,  4,   4,  5,   5,  5 ,  5,  5,   5,  5,  5,   5 ]






def note_status(freq):


    if freq:
        index = math.log(freq/F0,a)
    else:
        index = 0
   
    ## For cmdline loading GUI ##

    note_index = index %12
    notes_subscript_index = (index/12)
    
 
    if notes_subscript_index < 0:
        left_note = notes[int(note_index)] + str(eval('notes_subscript[int(note_index)] + int(abs(notes_subscript_index))-1'))
    else:
        
        left_note = notes[int(note_index)] + str(eval('notes_subscript[int(note_index)] + int(notes_subscript_index)'))
    right_note_index = int(note_index) + 1
    if right_note_index == 12:
        if notes_subscript_index < 0:
            right_note = notes[0] + str(eval('notes_subscript[0] + int(abs(notes_subscript_index))'))

        else:
            right_note = notes[0] + str(eval('notes_subscript[0] + int(notes_subscript_index) + 1'))
    else:
        if notes_subscript_index < 0:
            right_note = notes[right_note_index] +  str(eval('notes_subscript[right_note_index] + int(abs(notes_subscript_index))-1'))
        else:
            right_note = notes[right_note_index] +  str(eval('notes_subscript[right_note_index] + int(notes_subscript_index)'))



    bar_length = 100
    
    plus = '+'
    minus = '-'
    plus_length = int(bar_length * (note_index - int(note_index)))
    minus_length = bar_length - plus_length
    
    bar = plus * plus_length + minus * minus_length

    print(' '*130,end = '\r')
    print(left_note,bar,right_note,end='\r')






