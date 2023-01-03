# File: muisc_utils.py
# Function: module met diverse utility functies:
#           - Convert note to noteValue and
#           - convert noteValue to note
#           - set environment
# Author: cx1964

import music21 as m

def getNoteValue(noteName):
    # Convert a NoteName in a numeric value
    # In music a flat is notated as -
    # Bb = B-
    noteValues = { 
                   'C' : 0, 'B-' : 0, 
                   'C#': 1, 'D-' : 1,
                   'D' : 2, 'C##': 2,
                   'D#': 3, 'Eb' : 3,
                   'E' : 4,

                   'F' : 5, 'E#' : 5,
                   'F#': 6, 'G-' : 6,
                   'G' : 7, 'F##': 7,
                   'G#': 8, 'A-' : 8,
                   'A' : 9, 'B--': 9,
                   'A#':10, 'B-' :10,
                   'B' :11, 'C-' :11
                   # ToDo
                   # append all double sharps
                   # append all double flats
                 }
    return(noteValues[noteName.upper()])


def getNoteName(noteValue, enharmonic=False):
    # Convert a NoteValue in a string with a noteName
    # In music a flat is notated as -
    # Bb = B-
    if enharmonic==False:
        noteName = { 
                     0: 'C' ,  
                     1: 'C#',  
                     2: 'D' , 
                     3: 'D#', 
                     4: 'E' ,
                     5: 'F' , 
                     6: 'F#', 
                     7: 'G' , 
                     8: 'G#', 
                     9: 'A' , 
                    10: 'A#', 
                    11: 'B'  
                   }
    else:
        noteName = { 
                     0: 'B-' ,
                     1: 'D-' ,
                     2: 'C##',
                     3: 'Eb' ,
                     4: 'E'  , # because no enharmonic available. x =def enharmonic(x)
                     5: 'E#' ,
                     6: 'G-' ,
                     7: 'F##',
                     8: 'A-' ,
                     9: 'B--',
                    10: 'B-' ,
                    11: 'C-' 
                   # ToDo
                   # append all double sharps
                   # append all double flats
                   }                 
    return(noteName[noteValue])


def test_play_audio():
  import random
  keyDetune = []
  for i in range(127):
     keyDetune.append(random.randint(-30, 30))

  b = m.corpus.parse('bwv66.6')
  for n in b.flat.notes:
     n.pitch.microtone = keyDetune[n.pitch.midi]
  sp = m.midi.realtime.StreamPlayer(b)
  sp.play()    

def set_environment(p_MUSESCOREPROGPATH, p_MUSESCOREPROG):
    # See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html#usersguide-24-environment
    # See: https://web.mit.edu/music21/doc/usersGuide/usersGuide_24_environment.html
    env = m.environment.UserSettings()
    env.delete()
    env.create()
    # set environmment
    env['autoDownload'] = 'allow'
    #env['lilypondPath'] = '/usr/bin/lilypond'
    #env['musescoreDirectPNGPath'] = '/usr/bin/musescore3'
    env['musicxmlPath'] = p_MUSESCOREPROGPATH+p_MUSESCOREPROG


def get_aantal_half_steps_van_interval(intervalNaam):
    """
    Bepaalt het aantal halve toonafstanden voor gegeven interval.


    Returns Aantal halve toonafstanden als integer 
   
    Params
    intervalNaam   een string waarmee de intervalnaam mee gespecificeerd kan worden
                   mogelijke waarde
                   [ 'R1','v2','m2','O1','M2','v3','m3','O2','M3','v4','R4','O3',
                     'O4','v5','R5','v6','m6','O5','M6','v7','m7','O6','M7','v8',
                     'R8','O7']
    """
    
    #
    # List of intervals:
    # P1, d2 = 0 half-steps
    # m2, A1 = 1 half-step
    # M2, d3 = 2 half-steps
    # m3, A2 = 3 half-steps
    # M3, d4 = 4 half-steps
    # P4, A3 = 5 half-steps
    # A4, d5 = 6 half-steps
    # P5, d6 = 7 half-steps
    # m6, A5 = 8 half-steps
    # M6, d7 = 9 half-steps
    # m7, A6 = 10 half-steps
    # M7, d8 = 11 half-steps
    # P8, A7 = 12 half-steps
  
    # intervallen={  'k2': 1   # in 1/2 stappen
    #               ,'G2': 2
    #               ,'k3': 3
    #               ,'G3': 4}

    intervallen = {
                     'R1':  0 # 0 half-steps
                    ,'v2':  0 # 0 half-steps
                    ,'m2':  1 # half-step
                    ,'O1':  1 # half-step
                    ,'M2':  2 # half-steps
                    ,'v3':  2 # half-steps
                    ,'m3':  3 # half-steps
                    ,'O2':  3 # half-steps
                    ,'M3':  4 # half-steps
                    ,'v4':  4 # half-steps
                    ,'R4':  5 # half-steps
                    ,'O3':  5 # half-steps
                    ,'O4':  6 # half-steps
                    ,'v5':  6 # half-steps
                    ,'R5':  7 # half-steps
                    ,'v6':  7 # half-steps
                    ,'m6':  8 # half-steps
                    ,'O5':  8 # half-steps
                    ,'M6':  9 # half-steps
                    ,'v7':  9 # half-steps
                    ,'m7': 10 # half-steps
                    ,'O6': 10 # half-steps
                    ,'M7': 11 # half-steps
                    ,'v8': 11 # half-steps
                    ,'R8': 12 # half-steps
                    ,'O7': 12 # half-steps     
    }
    # debug               
    # i=intervallen['G3']
    return (intervallen[intervalNaam]) 

def play_interval(lNoot, hNoot):
    # Debug
    # print("debug functie play_interval")

    timeSignature = m.meter.TimeSignature('4/4')

    note1 = m.note.Note(lNoot, type='half')
    note2 = m.note.Note(hNoot, type='half')
    stream1 = m.stream.Stream()
    stream1.append(timeSignature)
    stream1.append(note1)
    stream1.append(note2)
    sp = m.midi.realtime.StreamPlayer(stream1)
    sp.play()  


def play_note(noot):
    # Debug
    # print("debug functie play_note")

    timeSignature = m.meter.TimeSignature('4/4')

    note1 = m.note.Note(noot, type='half')
    stream1 = m.stream.Stream()
    stream1.append(timeSignature)
    stream1.append(note1)
    sp = m.midi.realtime.StreamPlayer(stream1)
    sp.play() 

def generate_scale(tonic:str):
  '''
  Synopsis This function creates a scale based on a given tonic

  Arguments: 

    tonic: A string which defines the tonic of the scale. In this version the tonic can not have accidentals. 

  Returns:
    none: When incorrect tonic is provided
    scale: When a valid tonic is provided, this functions returns the notes of the scale as a List of strings 
  '''
  
  # initialisaties
  reeks = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  toonladder = list()
  start_index = 0 
  grondtoon = tonic

  # test arguments
  if (len(tonic) > 1) or (tonic not in reeks):
     print('Incorrect tonic: ', tonic)

     ### Temporary for this version
     if (len(tonic) >= 2) and (tonic[1] in ('#', 'b', '-')):
        print('Tonic can not have accidentals') 
     return(None)
     ### Temporary for this version

  if grondtoon != 'a':
    start = grondtoon  
    for i in range(0,7,1):
        if start == reeks[i]:
           # debug 
           # print(reeks[i])
           toonladder.append(reeks[i])
           start_index = i
        else:
           if  start_index != 0 :
               #  debug  
               # print(reeks[i])
               toonladder.append(reeks[i])
           i=i+1    
    huidige_lengte = len(toonladder)
  else:
    huidige_lengte = 0  
  # nog aanvullen na g en beginnen bij a

  #debug
  #print(toonladder)
  #print('lengte ', huidige_lengte )

  aantal_ontbrekende = 8 - huidige_lengte
  #debug
  #print('aantal_ontbrekende ', aantal_ontbrekende )
  
  toevoeging = reeks[0:aantal_ontbrekende]
  #debug
  #print(toevoeging)
  
  toonladder = toonladder+toevoeging
  
  if grondtoon == 'a':
     toonladder.append(grondtoon)

  return(toonladder)
# generate_scale


# Ionian     1  2  3  4  5  6  7  1   common (major scale)
# Dorian     1  2 ♭3  4  5  6 ♭7  1   common
# Phrygian   1 ♭2 ♭3  4  5 ♭6 ♭7  1   rare except Spanish and moorish
# Lydian     1  2  3 #4  5  6  7  1   rare except some Eastern and liturgical
# Mixolydian 1  2  3  4  5  6 ♭7  1   common
# Aeolian    1  2 ♭3  4  5 ♭6 ♭7  1   common (relative minor)
# Locrian    1 ♭2 ♭3  4 ♭5 ♭6 ♭7  1   very rare


def get_mode_properties(mode:str):
  # Doc: https://en.wikipedia.org/wiki/Mode_(music)
  '''
  Synopsis This function gets the properties of a given musical mode 

  Arguments: 

    mode: A string which defines a musical mode.
  
    The musical modes are:

      'ionian', 
      'hypo ..', 
      'dorian', 
      'hypodorian', 
      'phrygian', 
      'hypophrygian',  
      'lydian', 
      'hypo ..', 
      'mixolydian', 
      'hypo ..', 
      'aeolian', 
      'hypo ..', 
      'locrian', 
      'hypo ..', 

  Returns:
    The properties as a string of a given musical mode: When a valid mode is provided, this functions returns its properies
    The properties are:
    scaleDegrees
    dominantScaleDegree 
    finalis
    ambitius
    dominantScaleDegree 
  '''
  modes = {
        # betekenis symbolen in scaleDegrees:
        # - = mol = b = verlaging
        # # = kruis = verhoging

        'ionian'      : { 'finalis': 'c', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '' , '' , '' , '' , '' , '' , '' ]  } 
      #, 'hypo ..' 

       ,'dorian'      : { 'finalis': 'd', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '' , '-', '' , '' , '' , '-', '']  }
      #,'hypodorian'  : { 'finalis': 'd', 'ambititus': 'a-a', 'dominantScaleDegree': '3', 'scaleDegrees': ['' , '' , '' , '' , '' , '' , '' , '']  } 

       ,'phrygian'    : { 'finalis': 'e', 'ambititus': '1-1', 'dominantScaleDegree': '6', 'scaleDegrees': ['' , '-', '-', '' , '' , '-', '-', '']  } 
      #,'hypophrygian': { 'finalis': 'd', 'ambititus': 'a-a', 'dominantScaleDegree': '4', 'scaleDegrees': ['' , '' , '' , '' , '' , '' , '' , '']  } 

       ,'lydian'      : { 'finalis': 'f', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '' , '' , '#', '' , '' , '' , '']  } 
      #, 'hypo ..' 
                    
       ,'mixolydian'  : { 'finalis': 'g', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '' , '' , '' , '' , '' , '-', '']  } 
      #, 'hypo ..' 

       ,'aeolian'     : { 'finalis': 'a', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '' , '-', '' , '' , '-', '-', '']  } 
      #, 'hypo ..' 

       ,'locrian'     : { 'finalis': 'a', 'ambititus': '1-1', 'dominantScaleDegree': '5', 'scaleDegrees': ['' , '-', '-', '' , '-', '-', '-', '']  } 
      #, 'hypo ..' 
  }
  return(modes[mode])
# end set_mode_properties


def generate_mode(mode:str, finalis:str):
  # let op gebruik in eerste instantie een finalis zonder voortekens
  # test ook dat finalis geen voortekens heeft

  '''
  Synopsis This function generates a list of notes as strings of a given musical mode.

  Arguments
    mode: A given mode 
    finalis: The tonic of the musical mode 

  Returns
    A list of notes as a string of the musical mode.  
  ''' 

  count=0
  scale = list()
 
  modeProperties = get_mode_properties(mode)
  scaleDegrees = modeProperties['scaleDegrees']
  # debug
  # print ('in function <generate_mode> ', 'scaleDegrees:', scaleDegrees)


  gen_scale = generate_scale(finalis)

  # loop over de scaleDegrees
  for d in scaleDegrees:
    
    # Make note from scale degree d and accidental (=gen_scale[count]) 

    # debug:
    #print('scaleDegree: ',d)

    degree=gen_scale[count]
    noot = degree + d
    scale.append(noot)
    count=count+1
      
  return (scale)

# End generate_mode     