# File: t.py
# Function: python script voor experimenten
# Opmerking: 
#            

import music21 as m
import music_utils
from datetime import datetime
import random


# ###  BEGIN Instellingen ###
tonica='c'
mode='dorian'
minNumNotes = 8 # Is essential for well formed cantus firmus
maxNumNotes = 16 # Is essential for well formed cantus firmus
startOnTonic=True # True is essential for well formed cantus firmus 
stopOnTonic=True  # True is essential for well formed cantus firmus 










# ToDo
minNumNotes = 8 # Is essential for well formed cantus firmus
maxNumNotes = 16 # Is essential for well formed cantus firmus

key_signature = m.key.Key('C') #  lowercase = minor key.
numNotes=round(random.uniform(minNumNotes, maxNumNotes)) #
print('numNotes:', numNotes)



cf = music_utils.generate_modal_melody(mode, tonica, numNotes, startOnTonic, stopOnTonic)

def create_unique_maximum(numNotes:int, tonic:str, canta_firmus:list):
  posMax=random.uniform(0.25, 0.75)
  print('posMax:', posMax)
  locMax=round(numNotes*posMax) 
  print('loc:', locMax)
  
  # Bepaal en positioneer maxNote in cf
  scale = music_utils.generate_mode(mode, tonic)
  print('scale',scale)
  maxNote=scale[6]
  cf[locMax]=maxNote 

  print('cf orgineel:', cf)

  t=0
  for nt in cf:
    if (t != locMax):
      # Doe alleen iets als je niet op de positie van maxNote bent
      if (cf[t] == maxNote):
         # maak note lager om te zorgen dat er slechts 1 maxNote is
         cf[t] = scale[5]  
    t=t+1    

  return(locMax, maxNote, cf)

l,n,cf=create_unique_maximum(numNotes, tonica, cf)

print(l,n,cf)
         

 